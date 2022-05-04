"""Integration test utils."""
import json
from typing import Optional

from rdflib import Graph
from rdflib.compare import graph_diff, isomorphic


def get_skolem(base_url: str, count: int) -> str:
    """Get skolem according to base URL."""
    return base_url + ".well-known/skolem/" + str(count)


class SkolemUtils:
    """Testutils for mocking more than one skolemization."""

    skolemization_counter: int
    base_url: str

    def __init__(self, base_url: str) -> None:
        """Set up skolem utils."""
        self.skolemization_counter = 0
        self.base_url = base_url

    def get_skolemization(self) -> str:
        """Pops a skolemization from a stack of max 3 test skolemizations."""
        _skolemization = get_skolem(self.base_url, self.skolemization_counter)
        self.skolemization_counter = self.skolemization_counter + 1

        return _skolemization

    def reset_counter(self) -> None:
        """Reset skolemization counter."""
        self.skolemization_counter = 0


def prepare_model(model: str) -> dict:
    """Add necessary metadata for model mapping."""
    json_model: dict = json.loads(model)
    json_model["paths"] = {}
    for key in json_model.get("components", {}).get("schemas", {}).keys():
        json_model["paths"][key] = {
            "get": {
                "responses": {
                    "200": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": f"#/components/schemas/{key}"}
                            }
                        }
                    }
                }
            }
        }
    return json_model


def assert_isomorphic(g1: Graph, g2: Graph) -> None:
    """Compare two graphs an assert that they are isomorphic.

        If not isomorpic a graph diff will be dumped.

    Args:
        g1 (Graph): a graph to compare
        g2 (Graph): the graph to compare with

    """
    _isomorphic = isomorphic(g1, g2)
    if not _isomorphic:
        _dump_diff(g1, g2, None)
    assert _isomorphic


def _dump_diff(expected: Graph, actual: Graph, test_name: Optional[str]) -> None:
    in_both, in_first, in_second = graph_diff(expected, actual)
    print("\nin expected:")
    _dump_turtle(in_first)
    print("\nin actual:")
    _dump_turtle(in_second)
    if test_name:
        print(f"\ntest: {test_name}")


def _dump_turtle(g: Graph) -> None:
    for _l in g.serialize(format="turtle").splitlines():
        if _l:
            print(_l)
