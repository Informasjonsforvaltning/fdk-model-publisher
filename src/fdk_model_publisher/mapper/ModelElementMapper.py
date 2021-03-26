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
    extract_simple_type_restrictions,
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
        type = extract_type(properties, self.__endpoint_description)
        item_title = (
            title[0].upper() + title[1:]
            if title and type in ["codeList", "object", "simpleType"]
            else title
        )
        extended_path = deepcopy(path) + [item_title] if item_title else []
        identifier = build_identifier(item_title, self.__uri, extended_path)

        if identifier and identifier in self.__elements:
            return self.create_reference(properties, identifier)
        else:
            self.__elements.add(identifier)
            return self.create_element(item_title, properties, extended_path, type)

    def create_element(
        self, title: Optional[str], properties: Dict, path: List[str], type: str
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Model Element creators."""
        if type == "allOf":
            return self.handle_schema_combination(title, properties, path)
        elif type == "codeList":
            return self.create_code_list(title, properties, path)
        elif type == "object":
            return self.create_object_type(title, properties, path)
        elif type == "simpleType":
            return self.create_simple_type(
                properties.get("type"),
                title,
                extract_simple_type_restrictions(properties),
                path,
            )

        """Model Property creators."""
        if type == "array":
            return self.create_array_type(title, properties, path)
        elif type == "role":
            return self.create_role_type(title, properties, path)
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
            item = self.create_object_property(
                title=None, properties=properties, path=path
            )
            if item:
                schema_properties.append(item)

        object_type = ObjectType()
        object_type.identifier = build_identifier(
            title[0].upper() + title[1:] if title else None, self.__uri, extended_path
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

        reference = (
            self.map_item(**extract_ref_item(ref_string, self.__endpoint_description))
            if ref_string
            else None
        )

        composition = Composition()
        composition.identifier = build_identifier(title, self.__uri, path)
        composition.title = {"en": title} if title else {}
        composition.description = {"en": description} if description else {}
        if isinstance(reference, ObjectType):
            composition.contains = reference

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
        role.identifier = build_identifier(title, self.__uri, path)
        role.title = {"en": title} if title else {}
        role.description = {"en": description} if description else {}
        role.max_occurs = "1"
        role.min_occurs = (
            "1"
            if properties and title and title in properties.get("required", "")
            else "0"
        )

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
            reference = (
                self.map_item(
                    **extract_ref_item(ref_string, self.__endpoint_description)
                )
                if ref_string
                else None
            )

            if extracted_type == "codeList":
                attribute.has_value_from = (
                    reference if reference else self.map_item(title, properties, path)
                )

            if isinstance(reference, SimpleType):
                attribute.has_simple_type = reference
            else:
                type = "format" if "format" in properties.keys() else "type"
                type_string = properties.get(type)
                simple_type_type = type_string if type_string else ref_simple_type
                simple_type_restrictions = extract_simple_type_restrictions(properties)
                simple_type = self.create_simple_type(
                    simple_type_type,
                    None,
                    simple_type_restrictions,
                    path + [title]
                    if title and len(simple_type_restrictions.keys()) > 0
                    else None,
                )
                if simple_type:
                    attribute.has_simple_type = simple_type

        return attribute

    def create_simple_type(
        self,
        type: Optional[str],
        title: Optional[str] = None,
        restrictions: Optional[Dict] = None,
        path: Optional[List[str]] = None,
    ) -> Optional[SimpleType]:
        """Create simple type."""
        if restrictions is None:
            restrictions = {}
        simple_type = SimpleType()
        if title:
            simple_type.title = {"en": title}
            simple_type.identifier = (
                build_identifier(title, self.__uri, path)
                if path
                else f"{self.__uri}#{title}"
            )

        elif type:
            type_title = type[0].upper() + type[1:]
            simple_type.title = {"en": type_title}
            simple_type.identifier = (
                build_identifier(type_title, self.__uri, path)
                if path
                else f"{self.__uri}#{type_title}"
            )

        if type == "string":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#stringschema"
            )

            if "minLength" in restrictions:
                simple_type.min_length = restrictions["minLength"]
            if "maxLength" in restrictions:
                simple_type.max_length = restrictions["maxLength"]
            if "pattern" in restrictions:
                simple_type.pattern = restrictions["pattern"]

        elif type == "boolean":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#booleanschema"
            )
        elif type == "number":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#numberschema"
            )

            if "minimum" in restrictions:
                simple_type.min_inclusive = restrictions["minimum"]
            if "maximum" in restrictions:
                simple_type.min_exclusive = restrictions["maximum"]
            if "length" in restrictions:
                simple_type.length = restrictions["length"]
            if "totalDigits" in restrictions:
                simple_type.total_digits = restrictions["totalDigits"]
            if "fractionDigits" in restrictions:
                simple_type.fraction_digits = restrictions["fractionDigits"]

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
    ) -> Union[Role, Attribute, None]:
        """Create default array type."""
        description = properties.get("description", None)
        items = properties.get("items", {})
        item_type = extract_type(items, self.__endpoint_description)

        array_description = {"en": description} if description else {}
        max_occurs = properties.get("maxItems", "*")
        min_occurs = (
            "1"
            if title in properties.get("required", "")
            else str(properties.get("minItems", 0))
        )
        identifier = build_identifier(title, self.__uri, path)

        array = None
        if item_type == "role":
            array = self.map_item(title, items, path)
        elif item_type == "object":
            array = Role()
            object_title = title if title else title
            array.has_object_type = self.map_item(
                object_title, items, path + [title] if title else path
            )
        elif item_type == "allOf":
            item_properties = items.get("allOf", [])
            del items["allOf"]
            return self.create_default_array(
                title, {**items, "items": item_properties[0]}, path
            )
        else:
            array = self.create_attribute(title, items, path)

        if array:
            array.description = array_description
            array.max_occurs = max_occurs
            array.min_occurs = min_occurs
            array.identifier = identifier

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
                prop_title = str(key[0]).lower() + str(key[1:])
                item = self.create_object_property(
                    title=prop_title,
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

    def create_object_property(
        self, title: Optional[str], properties: dict, path: List[str]
    ) -> Union[ModelProperty, None]:
        """Create property for object."""
        extended_path = deepcopy(path) + [title] if title else path
        type = extract_type(properties, self.__endpoint_description)
        property_title = {"en": title} if title else {}
        description = properties.get("description", "")

        ref_string = properties.get("$ref", None)
        reference = (
            extract_ref_item(ref_string, self.__endpoint_description)
            if ref_string
            else None
        )

        if type == "object":
            object_prop = Composition()
            object_prop.identifier = build_identifier(title, self.__uri, extended_path)
            object_prop.title = property_title
            object_prop.description = {"en": description} if description else {}
            object_prop.max_occurs = "1"
            object_prop.min_occurs = (
                "1"
                if properties and title and title in properties.get("required", "")
                else "0"
            )
            if reference:
                object_prop.contains = self.map_item(**reference)
            else:
                object_prop.contains = self.map_item(title, properties, extended_path)
            return object_prop
        elif type == "codeList" or type == "simpleType":
            object_prop = Attribute()
            object_prop.identifier = build_identifier(title, self.__uri, extended_path)
            object_prop.title = property_title
            object_prop.description = {"en": description} if description else {}
            object_prop.max_occurs = "1"
            object_prop.min_occurs = (
                "1"
                if properties and title and (title in properties.get("required", ""))
                else "0"
            )
            if type == "codeList":
                if reference:
                    object_prop.has_value_from = self.map_item(**reference)
                else:
                    object_prop.has_value_from = self.map_item(
                        title, properties, extended_path
                    )
            else:
                if reference:
                    object_prop.has_simple_type = self.map_item(**reference)
                else:
                    object_prop.has_simple_type = self.map_item(
                        properties.get("type"), properties, extended_path
                    )
            return object_prop

        else:
            return self.map_item(title, properties, path)

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
