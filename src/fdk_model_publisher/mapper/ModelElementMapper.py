"""Model Element mapper."""

from copy import deepcopy
from typing import Dict, List, Optional, Union

from datacatalogtordf import URI
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
    extract_ref_item,
    extract_simple_type_restrictions,
    extract_type,
    extract_type_property,
    is_simple_type,
    nested_get,
    should_map,
)


class ModelElementMapper:
    """Model Element mapper class."""

    __endpoint_description: Dict
    __root_model: Dict
    __elements: Dict
    __uri: str

    def __setup(self, endpoint_description: Dict, uri: str) -> None:
        """Set up necessary variables for mapper."""
        self.__endpoint_description = endpoint_description
        schema = nested_get(endpoint_description, *["components", "schemas"])
        if schema and isinstance(schema, dict):
            self.__root_model = schema
            self.__uri = uri
            self.__elements = {}

    def extract_model_items(
        self, endpoint_description: Dict, uri: str
    ) -> List[ModelElement]:
        """Map and return model items from the supplied model."""
        model_elements = []
        self.__setup(endpoint_description, uri)

        if self.__uri and self.__root_model and self.__endpoint_description:
            paths = self.__endpoint_description.get("paths", {})
            for path in paths:
                schema = nested_get(
                    paths,
                    *[
                        path,
                        "get",
                        "responses",
                        "200",
                        "content",
                        "application/json",
                        "schema",
                    ],
                )
                if schema and isinstance(schema, dict):
                    ref_string = schema.get("$ref", "")
                    if ref_string and isinstance(ref_string, str):
                        model_elements.append(
                            self.map_item(
                                **extract_ref_item(
                                    ref_string, self.__endpoint_description
                                )
                            )
                        )
                    elif extract_type(schema, self.__endpoint_description) != "":
                        model_elements.append(self.map_item(None, schema, []))

        return list(
            filter(
                lambda item: isinstance(item, ModelElement) or isinstance(item, URI),
                model_elements,
            )
        )

    def map_item(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
        is_property: bool = False,
    ) -> Optional[Union[ModelElement, ModelProperty, URI]]:
        """Create model items (Elements and Properties) and references."""
        element_type = extract_type(
            properties, self.__endpoint_description, is_property
        )
        extended_path = deepcopy(path) + [title] if title else []
        path_string = "/".join(extended_path)

        if path_string and path_string in self.__elements:
            return URI(self.__elements[path_string])
        elif should_map(title, properties, is_property):
            element = self.create_element(
                title, properties, extended_path, element_type, is_property
            )
            return element
        else:
            return None

    def create_element(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
        element_type: str,
        is_property: bool,
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Model Element creators."""
        if element_type == "allOf":
            return self.handle_schema_combination(title, properties, path, is_property)
        elif element_type == "codeList":
            return self.create_code_list(title, properties, path)
        elif element_type == "object":
            return self.create_object_type(title, properties, path)
        elif is_simple_type(properties, is_property):
            return self.create_simple_type(title, properties, path)

        """Model Property creators."""
        if element_type == "array":
            return self.create_array_type(title, properties, path)
        elif element_type == "role":
            return self.create_role_type(title, properties, path)
        elif element_type == "composition":
            return self.create_composition(title, properties, path)
        elif element_type in ["string", "boolean", "number", "integer"]:
            return self.create_attribute(title, properties, path)

        return None

    def handle_schema_combination(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
        is_property: bool,
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Handle creation of items in allOf list."""
        schemas: List[Dict] = properties.get("allOf", [])
        description = properties.get("description", None)

        if len(schemas) > 1:
            return self.multi_schema_combination(
                title, description, schemas, path, is_property
            )

        elif len(schemas) == 1:
            schema_props = {
                key: properties[key] for key in properties if key != "allOf"
            }
            return self.single_schema_combination(
                title, schema_props, path, schemas[0], is_property
            )
        else:
            return None

    def single_schema_combination(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
        schema: dict,
        is_property: bool,
    ) -> Optional[Union[ModelElement, ModelProperty]]:
        """Handle creation of single item in allOf list."""
        description = properties.get("description", None)
        ref_string = schema.get("$ref", None)
        schema_type = extract_type(
            schema, self.__endpoint_description, is_property=is_property
        )

        if ref_string and not is_property:
            return self.map_item(
                **extract_ref_item(ref_string, self.__endpoint_description)
            )

        elif ref_string and schema_type == "role":
            return self.create_composition(title, {**properties, **schema}, path)

        elif ref_string and schema_type:
            return self.create_attribute(
                title,
                {"required": [title], "$ref": ref_string},
                path,
            )

        else:
            return self.map_item(
                title,
                {
                    "description": description,
                    "required": [title],
                    **schema.get("properties", {}),
                },
                path,
            )

    def multi_schema_combination(
        self,
        title: Optional[str],
        description: Optional[str],
        schemas: List[Dict],
        path: List[str],
        is_property: bool,
    ) -> Union[Composition, ObjectType]:
        """Create multi composition type element."""
        extended_path = deepcopy(path) + [title] if title else path

        object_type = ObjectType()
        object_type.identifier = self.create_model_identifier(
            title, extended_path if is_property else path
        )
        object_type.has_property = []

        for properties in schemas:
            item = self.map_item(
                title=None, properties=properties, path=path, is_property=True
            )
            if item:
                object_type.has_property.append(item)

        if is_property:

            composition = Composition()
            composition.identifier = self.create_model_identifier(title, path)
            composition.title = {"en": title} if title else {}
            composition.description = {"en": description} if description else {}
            composition.contains = object_type
            return composition

        else:
            object_type.title = {"en": title} if title else {}
            object_type.description = {"en": description} if description else {}
            return object_type

    def create_composition(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Composition:
        """Create composition type element."""
        description = properties.get("description")

        composition = Composition()
        composition.identifier = self.create_model_identifier(title, path)
        composition.title = {"en": title} if title else {}
        composition.description = {"en": description} if description else {}
        composition.max_occurs = "1"
        composition.min_occurs = (
            "1"
            if properties and title and title in properties.get("required", "")
            else "0"
        )
        ref_string = properties.get("$ref")
        if ref_string:
            reference = extract_ref_item(ref_string, self.__endpoint_description)
            composition.contains = self.map_item(**reference)
        elif extract_type(properties, self.__endpoint_description) == "object":
            composition.contains = self.map_item(title, properties, path)

        return composition

    def create_role_type(
        self,
        title: Optional[str],
        properties: Dict,
        path: List[str],
    ) -> Role:
        """Create Role type element."""
        description = properties.get("description", None)
        ref = properties.get("$ref")

        role = Role()
        role.identifier = self.create_model_identifier(title, path)
        role.title = {"en": title} if title else {}
        role.description = {"en": description} if description else {}
        role.max_occurs = "1"
        role.min_occurs = (
            "1"
            if properties and title and title in properties.get("required", "")
            else "0"
        )

        if ref and extract_type(properties, self.__endpoint_description) == "object":
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
        attribute.identifier = self.create_model_identifier(title, path)
        attribute.title = {"en": title} if title else {}
        attribute.description = {"en": description} if description else {}
        attribute.max_occurs = "1"
        attribute.min_occurs = (
            "1"
            if properties and title and (title in properties.get("required", ""))
            else "0"
        )

        if properties:
            attribute_type = extract_type(properties, self.__endpoint_description)
            ref_string = properties.get("$ref")

            if ref_string:
                reference = extract_ref_item(ref_string, self.__endpoint_description)
                if attribute_type == "codeList":
                    simple_type = extract_type_property(reference.get("properties", {}))
                    attribute.has_value_from = self.map_item(**reference)
                    attribute.has_simple_type = self.map_item(
                        None, {"type": simple_type}, path
                    )
                else:
                    attribute.has_simple_type = self.map_item(**reference)
            elif attribute_type == "codeList":
                simple_type = extract_type_property(properties)
                attribute.has_value_from = self.map_item(title, properties, path)
                attribute.has_simple_type = self.map_item(
                    None, {"type": simple_type}, path
                )
            else:
                attribute.has_simple_type = self.map_item(title, properties, path)

        return attribute

    def create_simple_type(
        self,
        title: Optional[str],
        properties: dict,
        path: List[str],
    ) -> Optional[SimpleType]:
        """Create simple type."""
        restrictions = extract_simple_type_restrictions(properties)
        type_path = path if path and len(restrictions.keys()) > 0 else []
        type_prop = extract_type(properties, self.__endpoint_description)

        simple_type = SimpleType()

        if type_prop == "string":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#stringschema"
            )

        elif type_prop == "boolean":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#booleanschema"
            )
        elif type_prop == "number":
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#numberschema"
            )

        elif type_prop in {"int32", "integer"}:
            simple_type.type_definition_reference = (
                "https://www.w3.org/2019/wot/json-schema#integerschema"
            )
        else:
            return None

        if "format" in properties:
            simple_type.title = {"en": properties.get("format")}
            simple_type.identifier = self.create_model_identifier(
                properties.get("format"), type_path
            )

        elif title and len(restrictions.keys()) > 0:
            simple_type.title = {"en": title}
            simple_type.identifier = self.create_model_identifier(title, type_path)

        elif type_prop:
            simple_type.title = {"en": properties.get("type")}
            simple_type.identifier = self.create_model_identifier(
                properties.get("type"), type_path
            )

        if restrictions:
            if "minLength" in restrictions:
                simple_type.min_length = restrictions["minLength"]
            if "maxLength" in restrictions:
                simple_type.max_length = restrictions["maxLength"]
            if "pattern" in restrictions:
                simple_type.pattern = restrictions["pattern"]
            if "minimum" in restrictions and not restrictions.get(
                "exclusiveMinimum", False
            ):
                simple_type.min_inclusive = restrictions["minimum"]
            if "maximum" in restrictions and not restrictions.get(
                "exclusiveMaximum", False
            ):
                simple_type.max_inclusive = restrictions["maximum"]
            if "length" in restrictions:
                simple_type.length = restrictions["length"]
            if "totalDigits" in restrictions:
                simple_type.total_digits = restrictions["totalDigits"]
            if "fractionDigits" in restrictions:
                simple_type.fraction_digits = restrictions["fractionDigits"]

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
        choice.identifier = self.create_model_identifier(title, path)
        choice.title = {"en": title} if title else {}
        choice.description = {"en": description} if description else {}
        choice.has_some = []
        choice.min_occurs = "1" if title in properties.get("required", "") else "0"
        choice.max_occurs = "*"

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
        items = properties.get("items", {})
        item_type = extract_type(items, self.__endpoint_description)
        ref_string = items.get("$ref")
        reference = (
            extract_ref_item(ref_string, self.__endpoint_description)
            if ref_string
            else None
        )
        description = items.get("description", None)

        array = Role() if item_type in {"object", "allOf", "array"} else Attribute()
        array.title = {"en": title} if title else {}
        array.identifier = self.create_model_identifier(title, path)
        array.description = {"en": description} if description else {}
        array.max_occurs = properties.get("maxItems", "*")
        array.min_occurs = (
            "1"
            if title and title in properties.get("required", "")
            else str(properties.get("minItems", 0))
        )

        if isinstance(array, Role) and reference:
            array.has_object_type = self.map_item(**reference)

        elif isinstance(array, Role) and item_type == "array":
            sub_array_title = title + "Array" if title else title
            array.has_object_type = self.create_object_type(
                sub_array_title,
                {"properties": {"items": items}},
                path,
            )
        elif isinstance(array, Role):
            array.has_object_type = self.map_item(title, items, path)
        elif reference and is_simple_type(reference.get("properties", {})):
            array.has_simple_type = self.map_item(**reference)
        elif is_simple_type(items):
            array.has_simple_type = self.map_item(title, items, path)

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

        object_type = ObjectType()
        object_type.identifier = self.create_model_identifier(title, path)
        object_type.title = {"en": title} if title else {}
        object_type.description = {"en": description} if description else {}

        if properties:
            object_type.has_property = []

            for key in properties.get("properties", {}):
                prop_title = str(key[0]).lower() + str(key[1:])
                prop_props = {
                    **properties["properties"][key],
                    "required": properties.get("required", []),
                }
                item = self.map_item(prop_title, prop_props, path, is_property=True)
                if isinstance(item, ModelProperty):
                    object_type.has_property.append(item)

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
        element.identifier = self.create_model_identifier(title, path)
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
        code_list.identifier = self.create_model_identifier(title, path)
        code_list.title = {"en": title} if title else {}
        code_list.description = {"en": description} if description else {}

        return code_list

    def create_model_identifier(self, title: Optional[str], path: List[str]) -> str:
        """Build identifier string."""
        if title:
            if len(path) > 1:
                path_string = "/".join(path[:-1])
                element_uri = f"{self.__uri}/{path_string}#{title}"
                self.__elements["/".join(path)] = element_uri
            else:
                element_uri = f"{self.__uri}#{title}"
                self.__elements[title] = element_uri

            return element_uri

        return ""
