import logging
import os
import re
from typing import Any, Dict, List, Optional

from datacatalogtordf import Agent, Catalog

from fdk_model_publisher.api.models import PartialInformationModel

from fdk_rdf_parser.classes import Publisher
from fdk_rdf_parser.fdk_rdf_parser import DataService
from modelldcatnotordf.modelldcatno import InformationModel
from modelldcatnotordf.modelldcatno import ModelElement, ModelProperty

FDK_MODEL_PUBLISHER_URI = os.getenv(
    "FDK_MODEL_PUBLISHER_URI", "https://fdk-model-publisher.fellesdatakatalog.no"
)


class Mapper:
    _im_prefix = {
        "nb": "Informasjonsmodell",
        "nn": "Informasjonsmodell",
        "en": "Information Model",
    }

    def __init__(self) -> None:
        self.master_map: Dict[str, ModelElement] = dict()

    def create_model_property(
        self, name: str, prop: Dict[str, Any], schema_uri: Optional[str]
    ) -> ModelProperty:
        model_property = ModelProperty()

        property_name = name
        if "$ref" in prop:
            ref: str = prop["$ref"]
            self.link_property_with_model(model_property, ref)
            # TODO: As such, this will collide with some ModelElement. Solution?: add _property ?
            property_name = ref.replace(
                "#/components/schemas/", ""
            )  # TODO?: + "_property"

        # TODO: just this one adds another ~3MB to the catalog in staging
        model_property.identifier = f"{schema_uri}#{property_name}"

        # the reason for if statements over get(key, default) is that
        # the 'empty' attributes for model_property should remain uninitialized
        if "minOccurs" in prop:
            model_property.min_occurs = prop["minOccurs"]

        if "maxOccurs" in prop:
            model_property.max_occurs = prop["maxOccurs"]

        return model_property

    def link_property_with_model(
        self, model_property: ModelProperty, ref_key: str
    ) -> None:
        model_element = self.master_map.get(ref_key, ModelElement())
        model_property.has_type.append(model_element)
        # store the reference to model_element, even if it is redundant
        # mainly because of the possible default value of map.get() earlier
        self.master_map[ref_key] = model_element

    def create_model_element(
        self, properties: Optional[Dict[str, Any]], uri: Optional[str], title: str
    ) -> ModelElement:

        ref_key = f"#/components/schemas/{title}"
        model_element = self.master_map.get(ref_key, ModelElement())
        # store the reference to model_element, even if it is redundant
        # mainly because of the possible default value of map.get() earlier
        self.master_map[ref_key] = model_element

        model_element.title = {"nb": title}
        model_element.identifier = f"{uri}#{title}"

        if properties:
            model_element.has_property = [
                self.create_model_property(k, v, schema_uri=uri)
                for k, v in properties.items()
            ]
        return model_element

    def from_partial_model(
        self, partial_model: PartialInformationModel, data_service: DataService
    ) -> Optional[InformationModel]:
        """Map schema object to InformationModel object."""
        if partial_model.schema is None:
            return None

        model = InformationModel()
        try:
            model_elements = partial_model.schema["components"]["schemas"]
            for title, element in model_elements.items():
                model.modelelements.append(
                    self.create_model_element(
                        properties=element.get("properties"),
                        uri=partial_model.endpoint_description,
                        title=title,
                    )
                )
        except KeyError as e:
            logging.error(e)
            return None

        model.identifier = partial_model.endpoint_description
        model.title = Mapper._prepend_model(data_service.title)
        model.keyword = data_service.keyword
        model.theme = data_service.theme
        model.description = data_service.description
        model.publisher = Mapper._extract_publisher(data_service.publisher)
        model.landing_page = data_service.landingPage
        model.language = data_service.language
        model.access_rights = (
            data_service.accessRights if data_service.accessRights else ""
        )
        model.conformsTo = (
            [resource.uri for resource in data_service.conformsTo]
            if data_service.conformsTo
            else None
        )

        return model

    @staticmethod
    def _prepend_model(
        multi_language_field: Optional[Dict[str, str]]
    ) -> Optional[Dict[str, str]]:
        if multi_language_field is None:
            return None

        return {
            field_language: f"{Mapper._im_prefix.get(field_language)} - {field_value}"
            for field_language, field_value in multi_language_field.items()
            if field_language in Mapper._im_prefix
        }

    @staticmethod
    def _extract_publisher(publisher: Optional[Publisher]) -> Optional[Agent]:
        if publisher and publisher.uri:
            matched = re.search(
                pattern=r"organizations/([0-9]{9})$", string=publisher.uri
            )
            if matched:
                organization_number = matched.group(1)
                agent = Agent()
                agent.organization_id = organization_number
                agent.identifier = f"{FDK_MODEL_PUBLISHER_URI}#{organization_number}"
                return agent
        return None

    @staticmethod
    def create_catalog(information_models: List[PartialInformationModel]) -> Catalog:
        # process all models that are not null into catalog
        catalog = Catalog()

        catalog.title = {"nb": "FDK informasjonsmodellkatalog"}
        catalog.identifier = FDK_MODEL_PUBLISHER_URI
        catalog.models = [model for model in information_models if model]
        return catalog
