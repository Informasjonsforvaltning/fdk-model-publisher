"""Integration test cases for the mapper service module."""
import json
from typing import Optional

from fdk_rdf_parser.fdk_rdf_parser import DataService
import pytest
from pytest_mock import MockFixture
from rdflib import Graph

from fdk_model_publisher.api.models import PartialInformationModel
from fdk_model_publisher.service.mapper import map_model_from_dict
from tests.integration.utils import _dump_diff, prepare_model, SkolemUtils
from tests.mocks.circular_dependencies_json import circular_dependencies_test_json
from tests.mocks.circular_dependencies_ttl import circular_dependencies_test_ttl
from tests.mocks.examples_json import (
    ex_1_json,
    ex_2_json,
    ex_3_json,
    ex_4_json,
    ex_5_json,
    ex_6_json,
    ex_7_json,
    ex_8_json,
    ex_9_json,
)
from tests.mocks.examples_ttl import (
    ex_10_ttl,
    ex_1_ttl,
    ex_2_ttl,
    ex_3_ttl,
    ex_4_ttl,
    ex_5_ttl,
    ex_6_ttl,
    ex_7_ttl,
    ex_8_ttl,
    ex_9_ttl,
)


def verify_model_from_json(
    model_str: str,
    expected_output_ttl: str,
    data_service: DataService,
    test_name: Optional[str],
    complete_json: bool = False,
) -> bool:
    """Model test helper function."""
    schema = json.loads(model_str) if complete_json else prepare_model(model_str)
    uri = list(data_service.endpointDescription)[0]
    info_model = PartialInformationModel(uri, schema)
    info_model.format = "JSON"
    model = map_model_from_dict(info_model, data_service)
    if model is not None:
        actual = Graph().parse(data=model.to_rdf(format="turtle"), format="turtle")
        expected = Graph().parse(data=expected_output_ttl, format="turtle")

        isomorphic = actual.isomorphic(expected)
        if isomorphic:
            return True
        else:
            _dump_diff(expected, actual, test_name)
            pass

            return False
    print("\nCOULD NOT MAP MODEL")
    return False


@pytest.mark.integration
def test_map_models_from_dict(mocker: MockFixture) -> None:
    """Assert that models are isomorphic to example."""
    base_url = "http://uri.com"
    ds_uri = "http://ds-uri.com"
    ds = DataService(
        title={"nb": "datatjeneste eksempler"},
        endpointDescription={base_url},
        uri=ds_uri,
    )
    skolemutils = SkolemUtils(base_url)

    mocker.patch(
        "skolemizer.Skolemizer.add_skolemization",
        side_effect=skolemutils.get_skolemization,
    )

    assert verify_model_from_json(ex_1_json, ex_1_ttl, ds, "ex_1")
    print("\nModel 1 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(ex_2_json, ex_2_ttl, ds, "ex_2")
    print("Model 2 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(ex_3_json, ex_3_ttl, ds, "ex_3")
    print("Model 3 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(ex_4_json, ex_4_ttl, ds, "ex_4")
    print("Model 4 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(ex_5_json, ex_5_ttl, ds, "ex_5")
    print("Model 5 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(ex_6_json, ex_6_ttl, ds, "ex_6")
    print("Model 6 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(ex_7_json, ex_7_ttl, ds, "ex_7")
    print("Model 7 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(ex_8_json, ex_8_ttl, ds, "ex_8")
    print("Model 8 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(ex_9_json, ex_9_ttl, ds, "ex_9")
    print("Model 9 passed.")

    skolemutils.reset_counter()

    ds_2 = DataService(
        title=ds.title,
        endpointDescription=ds.endpointDescription,
        uri="http://other-ds-uri.com",
    )

    assert verify_model_from_json(ex_9_json, ex_10_ttl, ds_2, "ex_10")
    print("\nModel 10 passed.")

    skolemutils.reset_counter()

    assert verify_model_from_json(
        circular_dependencies_test_json,
        circular_dependencies_test_ttl,
        ds,
        "circular_dependencies",
    )
    print("Handles circular dependencies.")

    skolemutils.reset_counter()
