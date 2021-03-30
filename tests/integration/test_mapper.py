"""Integration test cases for the mapper service module."""
import json

from fdk_rdf_parser.fdk_rdf_parser import DataService
import pytest
from pytest_mock import MockFixture
from rdflib import Graph

from fdk_model_publisher.api.models import PartialInformationModel
from fdk_model_publisher.service.mapper import map_model_from_dict
from tests.integration.utils import SkolemUtils, prepare_model
from tests.mocks.circular_dependencies_json import circular_dependencies_test_json
from tests.mocks.examples_json import (
    ex_1_json,
    ex_2_json,
    ex_3_json,
    ex_4_json,
    ex_5_json,
    ex_6_json,
    ex_7_json,
    ex_8_json,
)
from tests.mocks.circular_dependencies_ttl import circular_dependencies_test_ttl
from tests.mocks.examples_ttl import (
    ex_1_ttl,
    ex_2_ttl,
    ex_3_ttl,
    ex_4_ttl,
    ex_5_ttl,
    ex_6_ttl,
    ex_7_ttl,
    ex_8_ttl,
)

def verify_model(
    model_str: str, expected_output_ttl: str, data_service: DataService, complete_json: bool = False
) -> bool:
    """Model test helper function."""
    schema = json.loads(model_str) if complete_json else prepare_model(model_str)
    uri = list(data_service.endpointDescription)[0]
    info_model = PartialInformationModel(uri, schema)
    model = map_model_from_dict(info_model, data_service)
    if model is not None:
        actual = Graph().parse(data=model.to_rdf(format="turtle"), format="turtle")
        expected = Graph().parse(data=expected_output_ttl, format="turtle")

        isomorphic = actual.isomorphic(expected)
        if isomorphic:
            return True
        else:
            print("\nEXPECTED OUTPUT:")
            print(expected.serialize(format="turtle").decode("utf-8"))
            print("\nACTUAL OUTPUT:")
            print(actual.serialize(format="turtle").decode("utf-8"))
            return False
    print("\nCOULD NOT MAP MODEL")
    return False


@pytest.mark.integration
def test_map_models_from_dict(mocker: MockFixture) -> None:
    """Assert that models are isomorphic to example."""
    base_url = "http://uri.com"
    ds = DataService(
        title={"nb": "datatjeneste eksempler"}, endpointDescription={base_url}
    )
    skolemutils = SkolemUtils(base_url)

    mocker.patch(
        "modelldcatnotordf.skolemizer.Skolemizer.add_skolemization",
        side_effect=skolemutils.get_skolemization,
    )

    assert verify_model(ex_1_json, ex_1_ttl, ds)
    print("\nModel 1 passed.")

    skolemutils.reset_counter()

    assert verify_model(ex_2_json, ex_2_ttl, ds)
    print("Model 2 passed.")

    skolemutils.reset_counter()

    assert verify_model(ex_3_json, ex_3_ttl, ds)
    print("Model 3 passed.")

    skolemutils.reset_counter()

    assert verify_model(ex_4_json, ex_4_ttl, ds)
    print("Model 4 passed.")

    skolemutils.reset_counter()

    assert verify_model(ex_5_json, ex_5_ttl, ds)
    print("Model 5 passed.")

    skolemutils.reset_counter()

    assert verify_model(ex_6_json, ex_6_ttl, ds)
    print("Model 6 passed.")

    skolemutils.reset_counter()

    assert verify_model(ex_7_json, ex_7_ttl, ds)
    print("Model 7 passed.")

    skolemutils.reset_counter()

    assert verify_model(ex_8_json, ex_8_ttl, ds)
    print("Model 8 passed.")

    skolemutils.reset_counter()
