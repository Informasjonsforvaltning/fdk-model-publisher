import logging
import os
import re
from typing import Dict, List, Optional

from datacatalogtordf import Agent, Catalog

from fdk_model_publisher.api.models import PartialInformationModel

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.fdk_rdf_parser import DataService
from modelldcatnotordf.informationmodel import InformationModel
from modelldcatnotordf.modelelement import ModelElement

prepend_map = {
    "nb": "Informasjonsmodell",
    "nn": "Informasjonsmodell",
    "en": "Information Model",
}

FDK_MODEL_PUBLISHER_URL = os.getenv(
    "FDK_MODEL_PUBLISHER_URL", "https://fdk-model-publisher.fellesdatakatalog.no"
)


def prepend_model(
    multi_language_field: Optional[Dict[str, str]]
) -> Optional[Dict[str, str]]:
    if multi_language_field is None:
        return None

    return {
        field_language: f"{prepend_map.get(field_language)} - {field_value}"
        for field_language, field_value in multi_language_field.items()
        if field_language in prepend_map
    }


def extract_publisher(publisher: Optional[Publisher]) -> Optional[Agent]:
    if publisher and publisher.uri:
        matched = re.search(pattern=r"organizations/([0-9]{9})$", string=publisher.uri)
        if matched:
            organization_number = matched.group(1)
            agent = Agent()
            agent.organization_id = organization_number
            agent.identifier = f"{FDK_MODEL_PUBLISHER_URL}#{organization_number}"
            return agent
    return None


def create_model_element(uri: Optional[str], title: str) -> ModelElement:
    model_element = ModelElement()
    model_element.title = {"nb": title}
    model_element.identifier = f"{uri}#{title}"
    return model_element


def create_catalog(information_models: List[PartialInformationModel]) -> Catalog:
    # process all models that are not null into catalog
    catalog = Catalog()

    catalog.title = {"nb": "FDK informasjonsmodellkatalog"}
    catalog.identifier = "https://fdk-model-publisher.fellesdatakatalog.no"
    catalog.models = [model for model in information_models if model]
    return catalog


def map_model_from_dict(
    partial_model: PartialInformationModel, data_service: DataService
) -> Optional[InformationModel]:
    """Map schema object to InformationModel object."""
    if partial_model.schema is None:
        return None

    model = InformationModel()
    try:
        model_elements = partial_model.schema["components"]["schemas"]
        for title, _ in model_elements.items():
            model.modelelements.append(
                create_model_element(
                    uri=partial_model.endpoint_description, title=title
                )
            )
    except KeyError as e:
        logging.error(e)
        return None

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
