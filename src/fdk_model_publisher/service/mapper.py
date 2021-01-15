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
    uri: Optional[str],
    path: Optional[List[str]],
    root_model: dict,
) -> ObjectType:
    """Create object type."""
    object_type = ObjectType()
    object_type.title = {"en": title} if title else {}
    object_type.identifier = build_identifier(title, uri, path)
    if properties:
        property_items = [
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
            for key in properties.get("properties", {})
        ]
        object_type.has_property = filter(lambda item: item, property_items)

    return object_type


def create_simple_type(type: Optional[str], uri: Optional[str]) -> Optional[SimpleType]:
    """Create simple type."""
    simple_type = SimpleType()
    simple_type.title = {"en": type} if type else {}
    if type == "string":
        simple_type.identifier = f"{uri}#string"
        simple_type.type_definition_reference = (
            "https://www.w3.org/2019/wot/json-schema#stringschema"
        )
    elif type == "boolean":
        simple_type.identifier = f"{uri}#boolean"
        simple_type.type_definition_reference = (
            "https://www.w3.org/2019/wot/json-schema#booleanschema"
        )
    elif type == "number":
        simple_type.identifier = f"{uri}#number"
        simple_type.type_definition_reference = (
            "https://www.w3.org/2019/wot/json-schema#numberschema"
        )
    elif type == "int32":
        simple_type.identifier = f"{uri}#int32"
        simple_type.type_definition_reference = (
            "https://www.w3.org/2019/wot/json-schema#integerschema"
        )
    else:
        return None
    return simple_type


def create_attribute(
    title: Optional[str],
    properties: Optional[dict],
    uri: Optional[str],
    path: Optional[List[str]],
) -> Attribute:
    """Create model attribute."""
    attribute = Attribute()
    attribute.identifier = build_identifier(title, uri, path)
    attribute.title = {"en": title} if title else {}
    if properties:
        type = "format" if "format" in properties.keys() else "type"
        simple_type = create_simple_type(properties.get(type, None), uri)
        if simple_type:
            attribute.has_simple_type = simple_type

    attribute.min_occurs = (
        "1" if properties and title in properties.get("required", "") else "0"
    )
    attribute.max_occurs = "1"
    return attribute


def create_choice_type(
    title: Optional[str],
    properties: dict,
    uri: Optional[str],
    path: Optional[List[str]],
    root_model: Dict,
) -> ModelProperty:
    """Create model choice."""
    choice = Choice()
    choice.title = {"en": title} if title else {}
    choice.identifier = build_identifier(title, uri, path)
    one_of = []
    for item in nested_get(properties, "items", "oneOf"):
        choice_title = extract_ref_title(item.get("$ref"))
        if choice_title:
            one_of.append(
                create_object_type(
                    title=choice_title,
                    properties=None,
                    uri=uri,
                    path=[],
                    root_model=root_model,
                )
            )

    choice.has_some = one_of
    choice.min_occurs = (
        "1" if properties and title in properties.get("required", "") else "0"
    )
    choice.max_occurs = "1"
    return choice


def create_default_array(
    title: Optional[str],
    properties: dict,
    uri: Optional[str],
    path: Optional[List[str]],
    root_model: Dict,
) -> Optional[ModelProperty]:
    """Create default array type."""
    array = Role()
    array.title = {"en": title}
    array.identifier = build_identifier(title, uri, path)
    items = properties.get("items", None)

    if items:
        array_title = (
            extract_ref_title(items.get("$ref"))
            if "$ref" in items
            else title + "Array"
            if title
            else ""
        )
        array.has_object_type = create_object_type(
            title=array_title, properties=items, uri=uri, path=[], root_model=root_model
        )

    array.max_occurs = properties.get("maxItems", "*")
    array.min_occurs = (
        "1" if properties and title in properties.get("required", "") else "0"
    )
    return array


def create_array_type(
    title: Optional[str],
    properties: dict,
    uri: Optional[str],
    path: Optional[List[str]],
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
    properties: dict,
    uri: Optional[str],
    path: Optional[List[str]],
    root_model: dict,
) -> ModelProperty:
    """Create Role type element."""
    role = Role()
    role.title = {"en": title}
    role.identifier = build_identifier(title, uri, path)
    ref = properties.get("$ref", None)
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


def create_model_items(
    title: Optional[str],
    properties: dict,
    uri: Optional[str],
    path: Optional[List[str]],
    root_model: Dict,
) -> Optional[Union[ModelElement, ModelProperty]]:
    """Create model items (Elements and Properties)."""
    extended_path = deepcopy(path) + [title] if path and title else []
    if "$ref" in properties.keys():
        return create_role_type(title, properties, uri, extended_path, root_model)
    elif properties.get("type") == "object":
        return create_object_type(title, properties, uri, extended_path, root_model)
    elif properties.get("type") == "array":
        return create_array_type(title, properties, uri, extended_path, root_model)
    elif properties.get("type") == "string":
        return create_attribute(title, properties, uri, extended_path)
    elif properties.get("type") == "boolean":
        return create_attribute(title, properties, uri, extended_path)
    elif properties.get("type") == "number":
        return create_attribute(title, properties, uri, extended_path)
    elif properties.get("type") == "integer":
        return create_attribute(title, properties, uri, extended_path)
    else:
        return None


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

        for title, properties in schemas.items():
            model_item = create_model_items(
                title=title,
                properties=properties,
                uri=partial_model.endpoint_description,
                path=[],
                root_model=partial_model.schema,
            )

            if model_item:
                model_items.append(model_item)

    return model_items


def extract_ref_properties(ref: str, root_dict: Dict) -> Optional[Dict]:
    """Extract properties from ref link."""
    if ref.startswith("#/"):
        return nested_get(root_dict, *ref[2:].split("/"))
    return None


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


def nested_get(dct: Dict, *keys: str) -> Any:
    """Multi-level get helper function."""
    for key in keys:
        dct = dct.get(key, {})
    return dct


def build_identifier(
    title: Optional[str], uri: Optional[str], path: Optional[List[str]]
) -> str:
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
