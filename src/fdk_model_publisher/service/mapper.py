from typing import Dict, Optional

from fdk_rdf_parser.fdk_rdf_parser import DataService
from modelldcatnotordf.informationmodel import InformationModel

from api.models import PartialInformationModel

prepend = {
    "nb": "Informasjonsmodell",
    "nn": "Informasjonsmodell",
    "en": "Information Model",
}


def prepend_model(
    multi_language_field: Optional[Dict[str, str]]
) -> Optional[Dict[str, str]]:
    if multi_language_field is None:
        return None

    return {
        field_language: f"{prepend.get(field_language)} - {field_value}"
        for field_language, field_value in multi_language_field.items()
        if field_language in prepend
    }


def map_model_from_dict(
    raw: PartialInformationModel, data_service: DataService
) -> Optional[InformationModel]:
    """Map schema object to InformationModel object."""
    schema = raw.schema

    model = InformationModel()

    # TODO: should 'elements' exist or?
    # model.elements = ...
    # try:
    #     model.model_element = raw.schema['components']['schemas']
    # except KeyError as e:
    #     print(e)
    #     return None

    model.identifier = raw.endpointDescription
    model.title = prepend_model(data_service.title)
    model.keyword = data_service.keyword
    model.theme = data_service.theme
    model.description = data_service.description
    model.publisher = data_service.publisher
    model.landing_page = data_service.landingPage
    model.language = data_service.language
    model.access_rights = data_service.accessRights if data_service.accessRights else ""
    model.conformsTo = (
        [resource.uri for resource in data_service.conformsTo]
        if data_service.conformsTo
        else None
    )
    # model.contactpoint = data_service.contactPoint  # TODO: error

    return model
