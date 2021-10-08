"""JSON to TTL mapping."""
from hashlib import sha1
import re
from typing import Dict, List, Optional

from datacatalogtordf import Agent, Catalog
from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.fdk_rdf_parser import DataService
from modelldcatnotordf.modelldcatno import FoafDocument, InformationModel
from rdflib import Namespace

from fdk_model_publisher.api.models import PartialInformationModel
from fdk_model_publisher.config import Config
from fdk_model_publisher.mapper.ModelElementMapper import ModelElementMapper

model_element_mapper = ModelElementMapper()

MODELLDCATNO = Namespace("https://data.norge.no/vocabulary/modelldcatno#")

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


def generate_identifier(endpoint_description: str) -> str:
    """Generate ID for model."""
    return (
        Config.fdk_publishers_base_uri()
        + "/fdk-model-publisher/catalog/"
        + sha1(bytes(endpoint_description, encoding="utf-8")).hexdigest()  # noqa
    )


def map_model_from_dict(
    partial_model: PartialInformationModel, data_service: DataService
) -> Optional[InformationModel]:
    """Map schema object to InformationModel object."""
    if partial_model.schema is None or partial_model.endpoint_description is None:
        return None
    model = InformationModel()
    model_identifier = generate_identifier(partial_model.endpoint_description)
    model.modelelements = model_element_mapper.extract_model_items(
        partial_model.schema, model_identifier
    )

    foaf_document = FoafDocument(partial_model.endpoint_description)
    foaf_document.title = (
        {None: partial_model.title} if partial_model.title else None
    )
    if partial_model.format == "JSON":
        foaf_document.format = (
            "http://publications.europa.eu/resource/authority/file-type/JSON"
        )

    model.has_format.append(foaf_document)

    model.identifier = model_identifier
    model.title = prepend_model(data_service.title)
    model.keyword = data_service.keyword[0] if data_service.keyword else None
    model.theme = data_service.theme
    model.description = data_service.description
    model.publisher = extract_publisher(data_service.publisher)
    model.landing_page = data_service.landingPage
    model.language = data_service.language
    try:
        model.access_rights = data_service.accessRights.uri
    except (NameError, AttributeError):
        pass
    model.conformsTo = (
        [resource.uri for resource in data_service.conformsTo]
        if data_service.conformsTo
        else None
    )
    model.dct_type = "https://data.norge.no/vocabulary/modelldcatno#physicalModel"

    return model
