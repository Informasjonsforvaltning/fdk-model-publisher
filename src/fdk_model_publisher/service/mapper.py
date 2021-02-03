"""JSON to TTL mapping."""

from copy import deepcopy
import re
from typing import Any, Dict, List, Optional, Union

from datacatalogtordf import Agent, Catalog
from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.fdk_rdf_parser import DataService
from modelldcatnotordf.modelldcatno import (
    Attribute,
    Choice,
    CodeElement,
    CodeList,
    Composition,
    InformationModel,
    ModelElement,
    ModelProperty,
    ObjectType,
    Role,
    SimpleType,
)

from fdk_model_publisher.api.models import PartialInformationModel
from fdk_model_publisher.config import Config

prepend_map = {
    "nb": "Informasjonsmodell",
    "nn": "Informasjonsmodell",
    "en": "Information Model",
}


def prepend_model(
    multi_language_field: Optional[Dict[str, str]]
) -> Optional[Dict[str, str]]:
    """Prepend title with string."""
    if multi_language_field is None:
        return None

    return {
        field_language: f"{prepend_map.get(field_language)} - {field_value}"
        for field_language, field_value in multi_language_field.items()
        if field_language in prepend_map
    }


def create_catalog(information_models: List[PartialInformationModel]) -> Catalog:
    """Process all models that are not null into catalog."""
    catalog = Catalog()
    catalog.title = {"nb": "FDK informasjonsmodellkatalog"}
    catalog.identifier = Config.fdk_model_publisher_uri()
    catalog.models = [model for model in information_models if model]
    return catalog


def create_object_type(
    title: Optional[str],
    properties: Optional[dict],
    uri: str,
    path: List[str],
    root_model: Dict,
) -> ObjectType:
    """Create object type."""
    description = properties.get("description", None) if properties else {}

    object_type = ObjectType()
    object_type.title = {"en": title} if title else {}
    object_type.description = {"en": description} if description else {}
    if title and uri and path:
        object_type.identifier = build_identifier(title, uri, path)

    if properties:
        property_items = []
        for key in properties.get("properties", {}):
            property_items.extend(
                create_model_items(
                    title=key,
                    properties={
                        **properties["properties"][key],
                        "required": properties.get("required", []),
                    },
                    uri=uri,
                    path=path,
                    root_model=root_model,
                )
            )

        object_type.has_property = filter(lambda item: item, property_items)

    return object_type


def create_simple_type(
    type: Optional[str], uri: str, title: Optional[str] = None
) -> Optional[SimpleType]:
    """Create simple type."""
    simple_type = SimpleType()
    if title:
        simple_type.title = {"en": title}
        simple_type.identifier = f"{uri}#{title}"

    elif type:
        simple_type.title = {"en": type}
        simple_type.identifier = f"{uri}#{type}"

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


def create_attribute(
    title: Optional[str],
    properties: Optional[dict],
    uri: str,
    path: List[str],
    root_model: Dict,
) -> Attribute:
    """Create model attribute."""
    description = properties.get("description", None) if properties else {}

    attribute = Attribute()
    if title and uri and path:
        attribute.identifier = build_identifier(title, uri, path)
    attribute.title = {"en": title} if title else {}
    attribute.description = {"en": description} if description else {}

    if properties:
        ref_string = properties.get("$ref", "")
        ref_type = extract_ref_type(ref_string, root_model)
        ref_simple_type = extract_ref_properties(ref_string, root_model).get("type", "")
        reference = create_reference(ref_string, ref_type, uri)
        if reference and ref_type == "codeList":
            attribute.has_value_from = reference

        type = "format" if "format" in properties.keys() else "type"
        type_string = properties.get(type)
        simple_type = create_simple_type(
            type_string if type_string else ref_simple_type, uri
        )
        if simple_type:
            attribute.has_simple_type = simple_type

    attribute.min_occurs = (
        "1"
        if properties and title and (title in properties.get("required", ""))
        else "0"
    )
    attribute.max_occurs = "1"
    return attribute


def create_choice_type(
    title: Optional[str],
    properties: Dict,
    uri: str,
    path: List[str],
    root_model: Dict,
) -> Choice:
    """Create model choice."""
    description = properties.get("description", None)

    choice = Choice()
    choice.title = {"en": title} if title else {}
    choice.description = {"en": description} if description else {}
    if title and uri and path:
        choice.identifier = build_identifier(title, uri, path)

    one_of = []
    for item in nested_get(properties, "items", "oneOf"):
        ref_title = item.get("$ref")
        ref_type = extract_ref_type(ref_title, root_model)
        reference = create_reference(ref_title, ref_type, uri)
        if reference:
            one_of.append(reference)

    choice.has_some = one_of
    choice.min_occurs = (
        "1" if properties and title in properties.get("required", "") else "0"
    )
    choice.max_occurs = "1"
    return choice


def create_default_array(
    title: Optional[str],
    properties: Dict,
    uri: str,
    path: List[str],
    root_model: Dict,
) -> Optional[Role]:
    """Create default array type."""
    description = properties.get("description", None)
    items = properties.get("items", None)

    array = Role()
    array.title = {"en": title} if title else {}
    array.description = {"en": description} if description else {}
    if title and uri and path:
        array.identifier = build_identifier(title, uri, path)

    if items:
        ref_string = items.get("$ref")
        ref_type = extract_ref_type(ref_string, root_model)
        reference = create_reference(ref_string, ref_type, uri)
        if reference:
            array.has_object_type = reference
        else:
            extended_path = path + [title] if title else path
            array.has_object_type = create_object_type(
                title="items",
                properties=items,
                uri=uri,
                path=extended_path,
                root_model=root_model,
            )

    array.max_occurs = properties.get("maxItems", "*")
    array.min_occurs = (
        "1" if properties and title in properties.get("required", "") else "0"
    )
    return array


def create_array_type(
    title: Optional[str],
    properties: Dict,
    uri: str,
    path: List[str],
    root_model: Dict,
) -> Optional[ModelProperty]:
    """Create correct array type element."""
    if nested_get(properties, "items", "oneOf"):
        return create_choice_type(title, properties, uri, path, root_model)
    elif properties.get("items"):
        return create_default_array(title, properties, uri, path, root_model)
    else:
        return None


def create_role_type(
    title: Optional[str],
    properties: Dict,
    uri: str,
    path: List[str],
    root_model: Dict,
) -> Role:
    """Create Role type element."""
    description = properties.get("description", None)
    ref = properties.get("$ref", None)

    role = Role()
    role.title = {"en": title} if title else {}
    role.description = {"en": description} if description else {}
    if title and uri and path:
        role.identifier = build_identifier(title, uri, path)
    if ref:
        role.has_object_type = create_object_type(
            title=extract_ref_title(ref),
            properties=None,
            uri=uri,
            path=extract_ref_path(ref),
            root_model=root_model,
        )

    role.max_occurs = "1"

    role.min_occurs = (
        "1" if properties and title and title in properties.get("required", "") else "0"
    )
    return role


def create_multi_composition_type(
    title: Optional[str],
    description: Optional[str],
    properties: List[Dict],
    uri: str,
    path: List[str],
    root_model: Dict,
) -> List[Composition]:
    """Create multi composition type element."""
    extended_path = path + [title] if title else path

    all_of_props = []
    for prop in properties:
        ref_string = prop.get("$ref", None)
        ref_type = extract_ref_type(ref_string, root_model)
        ref_property = create_reference(ref_string, ref_type, uri)

        if ref_type == "object" and isinstance(ref_property, ModelElement):
            role_wrapper = Role()
            role_wrapper.has_object_type = ref_property
            all_of_props.append(role_wrapper)

        elif extract_type(prop, root_model) == "object":
            role_wrapper = Role()
            role_wrapper.has_object_type = create_object_type(
                None, prop, uri, extended_path, root_model
            )
            all_of_props.append(role_wrapper)

        elif ref_type and isinstance(ref_property, ModelProperty):
            all_of_props.append(ref_property)

        elif len(prop.keys()) > 0:
            all_of_props.extend(
                create_model_items(None, prop, uri, extended_path, root_model)
            )

    object_type = ObjectType()
    object_type.identifier = build_identifier(
        title.capitalize() if title else None, uri, extended_path
    )
    object_type.has_property = all_of_props

    composition = Composition()
    if title and uri and path:
        composition.identifier = build_identifier(title, uri, path)
    composition.title = {"en": title} if title else {}
    composition.description = {"en": description} if description else {}
    composition.contains = object_type

    return [composition]


def create_composition(
    title: Optional[str],
    properties: Dict,
    uri: str,
    ref_string: Optional[str],
    path: List[str],
) -> Composition:
    """Create composition type element."""
    description = properties.get("description")

    ref_obj = ObjectType()
    ref_obj.identifier = build_identifier(
        extract_ref_title(ref_string), uri, extract_ref_path(ref_string)
    )

    composition = Composition()
    if title and uri and path:
        composition.identifier = build_identifier(title, uri, path)
    composition.title = {"en": title} if title else {}
    composition.description = {"en": description} if description else {}
    composition.contains = ref_obj

    return composition


def handle_all_of_item(
    title: Optional[str],
    properties: Dict,
    uri: str,
    path: List[str],
    root_model: Dict,
) -> List[Union[ModelElement, ModelProperty]]:
    """Handle creation of items in allOf list."""
    all_of: List[Dict] = properties.get("allOf", [])
    description = properties.get("description", None)

    if len(all_of) > 1:
        return create_multi_composition_type(
            title, description, all_of, uri, path, root_model
        )

    else:
        ref_string = all_of[0].get("$ref", None)
        ref_type = extract_ref_type(ref_string, root_model)

        if ref_type == "object":
            return [create_composition(title, properties, uri, ref_string, path)]

        elif ref_type:
            return [
                create_attribute(
                    title,
                    {"required": [title], "$ref": ref_string},
                    uri,
                    path,
                    root_model,
                )
            ]

        else:
            return create_model_items(
                title,
                {"description": description, "required": [title], **all_of[0]},
                uri,
                path,
                root_model,
            )


def create_code_element(
    title: Optional[str],
    uri: str,
    path: List[str],
    parent: CodeList,
) -> CodeElement:
    """Create code element."""
    element = CodeElement()
    element.notation = title
    if title and uri and path:
        element.identifier = build_identifier(title, uri, path)
    element.in_scheme = [parent]
    return element


def create_code_list(
    title: Optional[str],
    properties: Dict,
    uri: str,
    path: List[str],
) -> List[Union[CodeList, CodeElement]]:
    """Create code list element."""
    description = properties.get("description", None)

    code_list = CodeList()
    code_list.title = {"en": title} if title else {}
    if title and uri and path:
        code_list.identifier = build_identifier(title, uri, path)
    code_list.description = {"en": description} if description else {}

    code_elements = [
        create_code_element(element, uri, path, code_list)
        for element in properties.get("enum", [])
    ]

    return [code_list] + code_elements


def create_model_items(
    title: Optional[str],
    properties: Dict,
    uri: str,
    path: List[str],
    root_model: Dict,
) -> List[Union[ModelElement, ModelProperty]]:
    """Create model items (Elements and Properties)."""
    extended_path = deepcopy(path) + [title] if title else []
    type = extract_type(properties, root_model)

    """Model Element creators."""
    if type == "allOf":
        return handle_all_of_item(title, properties, uri, extended_path, root_model)
    elif type == "role":
        return [create_role_type(title, properties, uri, extended_path, root_model)]
    elif type == "codeList":
        return create_code_list(title, properties, uri, extended_path)
    elif type == "object":
        return [create_object_type(title, properties, uri, extended_path, root_model)]
    elif len(properties.keys()) == 1 and properties.get("type"):
        return [create_simple_type(properties.get("type"), uri, title)]

    """Model Property creators."""
    if type == "array":
        return [create_array_type(title, properties, uri, extended_path, root_model)]
    elif type in ["string", "boolean", "number", "integer"]:
        return [create_attribute(title, properties, uri, extended_path, root_model)]

    return []


def create_reference(
    ref: str, type: str, uri: str
) -> Optional[Union[ModelElement, ModelProperty]]:
    """Create reference to object in graph."""
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

    reference.identifier = extract_ref_uri(ref, uri)

    return reference


def extract_publisher(publisher: Optional[Publisher]) -> Optional[Agent]:
    """Extract publisher."""
    if publisher and publisher.uri:
        matched = re.search(pattern=r"organizations/([0-9]{9})$", string=publisher.uri)
        if matched:
            organization_number = matched.group(1)
            agent = Agent()
            agent.organization_id = organization_number
            agent.identifier = (
                f"{Config.fdk_model_publisher_uri()}#{organization_number}"
            )
            return agent
    return None


def extract_model_items(
    partial_model: PartialInformationModel,
) -> List[Union[ModelElement, ModelProperty]]:
    """Extract model items from information model."""
    model_items = []
    if partial_model.schema:
        schemas = partial_model.schema.get("components", {}).get("schemas", {})
        uri = partial_model.endpoint_description

        for title, properties in schemas.items():
            model_item = create_model_items(
                title=title,
                properties=properties,
                uri=uri if uri else "",
                path=[],
                root_model=partial_model.schema,
            )

            if model_item:
                model_items.extend(model_item)

    return model_items


def extract_ref_properties(ref: str, root_dict: Dict) -> Dict:
    """Extract properties from ref link."""
    if ref.startswith("#/"):
        return nested_get(root_dict, *ref[2:].split("/"))
    return {}


def extract_ref_title(ref: Optional[str]) -> Optional[str]:
    """Extract title from ref string."""
    if ref and ref.startswith("#/"):
        return ref.split("/")[-1]
    else:
        return None


def extract_ref_path(ref: Optional[str]) -> List[str]:
    """Extract path to object from ref."""
    if ref and ref.startswith("#/"):
        return (
            ref.split("/")[3:]
            if ref.startswith("#/components/schemas/")
            else ref.split("/")
        )
    else:
        return []


def extract_ref_uri(ref: Optional[str], uri: str) -> Optional[str]:
    """Extract uri from ref."""
    if uri and ref and ref.startswith("#/components/schemas/"):
        return f"{uri}#{ref[21:]}"
    else:
        return ""


def extract_ref_type(ref: Optional[str], root_model: Dict) -> str:
    """Extract type from ref object."""
    if ref and ref.startswith("#/"):
        keys = ref.split("/")[1:]
        ref_object = nested_get(root_model, *keys)

        if isinstance(ref_object, Dict):
            return extract_type(ref_object, root_model)

    return ""


def extract_type(properties: Dict, root_model: Dict) -> str:
    """Extract type from property dictionary."""
    prop_type = properties.get("type", "")
    prop_keys = properties.keys()
    if "allOf" in prop_keys:
        return "allOf"
    elif "$ref" in prop_keys:
        ref_type = extract_ref_type(properties.get("$ref"), root_model)
        if ref_type == "object":
            return "role"
        return ref_type
    elif "enum" in prop_keys:
        return "codeList"
    else:
        return prop_type


def nested_get(dct: Dict, *keys: str) -> Any:
    """Multi-level get helper function."""
    for key in keys:
        dct = dct.get(key, {})
    return dct


def build_identifier(title: Optional[str], uri: str, path: List[str]) -> str:
    """Build identifier string."""
    if path and len(path) > 1:
        path_string = "/".join(path[:-1])
        return f"{uri}/{path_string}#{title}"
    else:
        return f"{uri}#{title}"


def map_model_from_dict(
    partial_model: PartialInformationModel, data_service: DataService
) -> Optional[InformationModel]:
    """Map schema object to InformationModel object."""
    if partial_model.schema is None:
        return None

    model = InformationModel()
    model.modelelements = extract_model_items(partial_model)
    model.identifier = partial_model.endpoint_description
    model.title = prepend_model(data_service.title)
    model.keyword = data_service.keyword
    model.theme = data_service.theme
    model.description = data_service.description
    model.publisher = extract_publisher(data_service.publisher)
    model.landing_page = data_service.landingPage
    model.language = data_service.language
    model.access_rights = data_service.accessRights if data_service.accessRights else ""
    model.conformsTo = (
        [resource.uri for resource in data_service.conformsTo]
        if data_service.conformsTo
        else None
    )

    return model
