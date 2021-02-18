"""JSON to TTL mapping."""
import logging
import re
from typing import Dict, List, Optional

from datacatalogtordf import Agent, Catalog
from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.fdk_rdf_parser import DataService
from modelldcatnotordf.modelldcatno import InformationModel

from fdk_model_publisher.api.models import PartialInformationModel
from fdk_model_publisher.config import Config
from fdk_model_publisher.mapper.ModelElementMapper import ModelElementMapper

model_element_mapper = ModelElementMapper()

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


def map_model_from_dict(
    partial_model: PartialInformationModel, data_service: DataService
) -> Optional[InformationModel]:
    """Map schema object to InformationModel object."""
    logging.info(
        f"Mapping {data_service.title} model from {partial_model.endpoint_description}"
    )
    if partial_model.schema is None or partial_model.endpoint_description is None:
        return None
    model = InformationModel()
    model.modelelements = model_element_mapper.extract_model_items(
        partial_model.schema, partial_model.endpoint_description
    )
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
