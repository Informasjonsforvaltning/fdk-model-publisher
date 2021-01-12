"""JSON to TTL mapping."""

import re
from typing import Dict, List, Optional, Union

from datacatalogtordf import Agent, Catalog
from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.fdk_rdf_parser import DataService
from modelldcatnotordf.modelldcatno import (
    Attribute,
    InformationModel,
    ModelElement,
    ModelProperty,
    ObjectType,
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
    title: str, properties: Optional[dict], uri: Optional[str]
) -> ObjectType:
    """Create object type."""
    model_element = ObjectType()
    model_element.title = {"en": title}
    model_element.identifier = f"{uri}#{title}"
    if properties:
        property_items = [
            create_model_items(
                key,
                {
                    **properties["properties"][key],
                    "required": properties.get("required", []),
                },
                uri,
            )
            for key in properties.get("properties", {})
        ]
        model_element.has_property = filter(lambda item: item, property_items)
    return model_element


def create_simple_type(type: str, uri: Optional[str]) -> Optional[SimpleType]:
    """Create simple type."""
    simple_type = SimpleType()
    simple_type.title = {"en": type}
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
    else:
        return None
    return simple_type


def create_attribute(
    title: str, properties: Optional[dict], uri: Optional[str]
) -> Attribute:
    """Create model attribute."""
    attribute = Attribute()
    attribute.identifier = f"{uri}#{title}"
    attribute.title = {"en": title}
    if properties:
        simple_type = create_simple_type(properties["type"], uri)
        if simple_type:
            attribute.has_simple_type = simple_type

    attribute.min_occurs = (
        "1" if properties and title in properties.get("required", "") else "0"
    )
    attribute.max_occurs = "1"
    return attribute


def create_model_items(
    title: str, properties: dict, uri: Optional[str]
) -> Optional[Union[ModelElement, ModelProperty]]:
    """Create model items (Elements and Properties)."""
    if properties.get("type") == "object":
        return create_object_type(title, properties, uri)
    elif properties.get("type") == "array":
        # TODO Code list
        return None
    elif properties.get("type") == "string":
        return create_attribute(title, properties, uri)
    elif properties.get("type") == "boolean":
        return create_attribute(title, properties, uri)
    elif properties.get("type") == "number":
        return create_attribute(title, properties, uri)
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
            )

            if model_item:
                model_items.append(model_item)

    return model_items


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
