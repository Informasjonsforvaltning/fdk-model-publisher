"""Model Element mapper."""

from copy import deepcopy
from typing import Dict, List, Optional, Set, Union

from modelldcatnotordf.modelldcatno import (
    Attribute,
    Choice,
    CodeElement,
    CodeList,
    Composition,
    ModelElement,
    ModelProperty,
    ObjectType,
    Role,
    SimpleType,
)

from fdk_model_publisher.mapper.utils import (
    build_identifier,
    extract_ref_item,
    extract_ref_uri,
    extract_type,
    nested_get,
)


class ModelElementMapper:
    """Model Element mapper class."""

    __endpoint_description: Dict
    __root_model: Dict
    __elements: Set
    __uri: str

    def __setup(self, endpoint_description: Dict, uri: str) -> None:
        """Set up necessary variables for mapper."""
        self.__endpoint_description = endpoint_description
        schema = nested_get(endpoint_description, *["components", "schemas"])
        if schema and isinstance(schema, dict):
            self.__root_model = schema
            self.__uri = uri
            self.__elements = set()

    def extract_model_items(
        self, endpoint_description: Dict, uri: str
    ) -> List[ModelElement]:
        """Map and return model items from the supplied model."""
        model_elements = []
        self.__setup(endpoint_description, uri)

        if self.__uri and self.__root_model and self.__endpoint_description:
            paths = self.__endpoint_description.get("paths", {})
            for path in paths:
                reference = nested_get(
                    paths,
                    *[
                        path,
                        "get",
                        "responses",
                        "200",
                        "content",
                        "application/json",
                        "schema",
                        "$ref",
                    ],
                )
                if reference and isinstance(reference, str):
                    model_elements.append(
                        self.map_item(
                            **extract_ref_item(reference, self.__endpoint_description)
                        )
                    )

        return list(filter(lambda item: isinstance(item, ModelElement), model_elements))

    def map_item(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Create model items (Elements and Properties) and references."""
        extended_path = deepcopy(path) + [title] if title else []
        identifier = build_identifier(title, self.__uri, extended_path)

        if identifier and identifier in self.__elements:
            return self.create_reference(properties, identifier)
        else:
            self.__elements.add(identifier)
            return self.create_element(title, properties, extended_path)

    def create_element(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Model Element creators."""
        type = extract_type(properties, self.__endpoint_description)

        if type == "allOf":
            return self.handle_schema_combination(title, properties, path)
        elif type == "codeList":
            return self.create_code_list(title, properties, path)
        elif type == "role":
            return self.create_role_type(title, properties, path)
        elif type == "object":
            return self.create_object_type(title, properties, path)
        elif len(properties.keys()) == 1 and properties.get("type"):
            return self.create_simple_type(properties.get("type"), title)

        """Model Property creators."""
        if type == "array":
            return self.create_array_type(title, properties, path)
        elif type in ["string", "boolean", "number", "integer"]:
            return self.create_attribute(title, properties, path)

        return None

    def create_reference(
        self, properties: dict, identifier: str
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Create reference to object in graph."""
        type = extract_type(properties, self.__endpoint_description)
        if type == "object":
            reference = ObjectType()
        elif type == "codeList":
            reference = CodeList()
        elif type == "oneOf":
            reference = Choice()
        elif type == "items":
            reference = Role()
        elif type in ["string", "boolean", "number", "integer"]:
            reference = Attribute()
        else:
            return None

        reference.identifier = identifier

        return reference

    def handle_schema_combination(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Handle creation of items in allOf list."""
        schemas: List[Dict] = properties.get("allOf", [])
        description = properties.get("description", None)

        if len(schemas) > 1:
            return self.multi_schema_combination(title, description, schemas, path)

        elif len(schemas) == 1:
            return self.single_schema_combination(title, properties, path, schemas[0])
        else:
            return None

    def single_schema_combination(
        self, title: Optional[str], properties: Dict, path: List[str], schema: dict
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Handle creation of single item in allOf list."""
        description = properties.get("description", None)
        ref_string = schema.get("$ref", None)
        ref_type = extract_type(schema, self.__endpoint_description)

        if ref_type == "role":
            return self.create_composition(title, properties, ref_string, path)

        elif ref_type:
            return self.create_attribute(
                title,
                {"required": [title], "$ref": ref_string},
                path,
            )

        else:
            return self.map_item(
                title,
                {"description": description, "required": [title], **schema},
                path,
            )

    def multi_schema_combination(
        self,
        title: Optional[str],
        description: Optional[str],
        schemas: List[Dict],
        path: List[str],
    ) -> Composition:
        """Create multi composition type element."""
        extended_path = path + [title] if title else path
        schema_properties = []

        for properties in schemas:
            type = extract_type(properties, self.__endpoint_description)
            reference = self.map_item(
                **extract_ref_item(
                    properties.get("$ref", ""), self.__endpoint_description
                )
            )

            if type == "object":
                role_wrapper = Role()
                role_wrapper.has_object_type = (
                    reference
                    if reference
                    else self.create_object_type(None, properties, extended_path)
                )
                schema_properties.append(role_wrapper)

            elif type and reference:
                schema_properties.append(reference)

            elif len(properties.keys()) > 0:
                item = self.map_item(None, properties, extended_path)
                if item:
                    schema_properties.append(item)

        object_type = ObjectType()
        object_type.identifier = build_identifier(
            title.capitalize() if title else None, self.__uri, extended_path
        )
        object_type.has_property = schema_properties

        composition = Composition()
        composition.identifier = build_identifier(title, self.__uri, path)
        composition.title = {"en": title} if title else {}
        composition.description = {"en": description} if description else {}
        composition.contains = object_type

        return composition

    def create_composition(
        self,
        title: Optional[str],
        properties: Dict,
        ref_string: str,
        path: List[str],
    ) -> Composition:
        """Create composition type element."""
        description = properties.get("description")

        ref_obj = ObjectType()
        ref_obj.identifier = extract_ref_uri(ref_string, self.__uri)

        composition = Composition()
        composition.title = {"en": title} if title else {}
        composition.description = {"en": description} if description else {}
        composition.contains = ref_obj
        composition.identifier = build_identifier(title, self.__uri, path)

        return composition

    def create_role_type(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Role:
        """Create Role type element."""
        description = properties.get("description", None)
        ref = properties.get("$ref", "")

        role = Role()
        role.title = {"en": title} if title else {}
        role.description = {"en": description} if description else {}
        role.max_occurs = "1"
        role.min_occurs = (
            "1"
            if properties and title and title in properties.get("required", "")
            else "0"
        )

        role.identifier = build_identifier(title, self.__uri, path)
        if ref:
            role.has_object_type = self.map_item(
                **extract_ref_item(ref, self.__endpoint_description)
            )
        return role

    def create_attribute(
        self,
        title: Optional[str],
        properties: Optional[dict],
        path: List[str],
    ) -> Attribute:
        """Create model attribute."""
        description = properties.get("description", None) if properties else {}

        attribute = Attribute()
        attribute.title = {"en": title} if title else {}
        attribute.description = {"en": description} if description else {}
        attribute.max_occurs = "1"
        attribute.min_occurs = (
            "1"
            if properties and title and (title in properties.get("required", ""))
            else "0"
        )
        attribute.identifier = build_identifier(title, self.__uri, path)

        if properties:
            ref_string = properties.get("$ref", "")
            extracted_type = extract_type(properties, self.__endpoint_description)
            ref_simple_type = nested_get(
                extract_ref_item(ref_string, self.__endpoint_description),
                *["properties", "type"],
            )
            reference = self.map_item(
                **extract_ref_item(ref_string, self.__endpoint_description)
            )
            if reference and extracted_type == "codeList":
                attribute.has_value_from = reference

            type = "format" if "format" in properties.keys() else "type"
            type_string = properties.get(type)
            simple_type = self.create_simple_type(
                type_string if type_string else ref_simple_type
            )
            if simple_type:
                attribute.has_simple_type = simple_type

        return attribute

    def create_simple_type(
        self, type: Optional[str], title: Optional[str] = None
    ) -> Optional[SimpleType]:
        """Create simple type."""
        simple_type = SimpleType()
        if title:
            simple_type.title = {"en": title}
            simple_type.identifier = f"{self.__uri}#{title}"

        elif type:
            simple_type.title = {"en": type}
            simple_type.identifier = f"{self.__uri}#{type}"

        if type == "string":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#stringschema"
            )
        elif type == "boolean":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#booleanschema"
            )
        elif type == "number":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#numberschema"
            )
        elif type == "int32" or type == "integer":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#integerschema"
            )
        else:
            return None
        return simple_type

    def create_choice_type(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Choice:
        """Create model choice."""
        description = properties.get("description", None)

        choice = Choice()
        choice.title = {"en": title} if title else {}
        choice.description = {"en": description} if description else {}
        choice.has_some = []
        choice.min_occurs = "1" if title in properties.get("required", "") else "0"
        choice.max_occurs = "*"
        choice.identifier = build_identifier(title, self.__uri, path)

        items = nested_get(properties, *["items", "oneOf"])
        if items:
            for item in items:
                ref_string = item.get("$ref")
                reference = self.map_item(
                    **extract_ref_item(ref_string, self.__endpoint_description)
                )
                if reference:
                    choice.has_some.append(reference)

        return choice

    def create_default_array(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Role:
        """Create default array type."""
        description = properties.get("description", None)
        items = properties.get("items", None)

        array = Role()
        array.title = {"en": title} if title else {}
        array.description = {"en": description} if description else {}
        array.max_occurs = properties.get("maxItems", "*")
        array.min_occurs = "1" if title in properties.get("required", "") else "0"

        array.identifier = build_identifier(title, self.__uri, path)

        if items:
            ref_string = items.get("$ref", "")
            reference = self.map_item(
                **extract_ref_item(ref_string, self.__endpoint_description)
            )
            if reference:
                array.has_object_type = reference
            else:
                extended_path = path + [title] if title else path
                array.has_object_type = self.create_object_type(
                    title="items",
                    properties=items,
                    path=extended_path,
                )

        return array

    def create_array_type(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Optional[ModelProperty]:
        """Create correct array type element."""
        if nested_get(properties, "items", "oneOf"):
            return self.create_choice_type(title, properties, path)
        elif properties.get("items"):
            return self.create_default_array(title, properties, path)
        else:
            return None

    def create_object_type(
        self,
        title: Optional[str],
        properties: Optional[dict],
        path: List[str],
    ) -> ObjectType:
        """Create object type."""
        description = properties.get("description", None) if properties else {}
        property_items = []

        if properties:
            for key in properties.get("properties", {}):
                item = self.map_item(
                    title=key,
                    properties={
                        **properties["properties"][key],
                        "required": properties.get("required", []),
                    },
                    path=path,
                )
                if item:
                    property_items.append(item)

        object_type = ObjectType()
        object_type.title = {"en": title} if title else {}
        object_type.description = {"en": description} if description else {}
        object_type.has_property = property_items
        object_type.identifier = build_identifier(title, self.__uri, path)
        return object_type

    def create_code_element(
        self,
        title: Optional[str],
        path: List[str],
        parent: CodeList,
    ) -> CodeElement:
        """Create code element."""
        element = CodeElement()
        element.notation = title
        element.identifier = build_identifier(title, self.__uri, path)
        element.in_scheme = [parent]
        return element

    def create_code_list(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> CodeList:
        """Create code list element."""
        description = properties.get("description", None)

        code_list = CodeList()
        code_list.title = {"en": title} if title else {}
        code_list.identifier = build_identifier(title, self.__uri, path)
        code_list.description = {"en": description} if description else {}

        return code_list
