"""Unit test cases for the mapper service module."""
import json

from fdk_rdf_parser.fdk_rdf_parser import DataService
import pytest
from rdflib import Graph

from fdk_model_publisher.api.models import PartialInformationModel
from fdk_model_publisher.service.mapper import map_model_from_dict
from tests.mocks.examples_json import ex_1_json
from tests.mocks.examples_ttl import ex_1_ttl


def verify_model(
    input_location: str, expected_output_ttl: str, data_service: DataService
) -> bool:
    """Model test helper function."""
    schema = json.loads(input_location)
    info_model = PartialInformationModel(data_service.endpointDescription[0], schema)
    model = map_model_from_dict(info_model, data_service)
    if model is not None:
        actual = Graph().parse(data=model.to_rdf(format="turtle"), format="turtle")
        expected = Graph().parse(data=expected_output_ttl, format="turtle")

        return actual.isomorphic(expected)
    return False


@pytest.mark.unit
def test_map_models_from_dict() -> None:
    """Assert that models are isomorphic to example."""
    ds = DataService(
        title={"nb": "eksempel 1"}, endpointDescription=["http://www.validuri.com"]
    )
    assert verify_model(ex_1_json, ex_1_ttl, ds)
