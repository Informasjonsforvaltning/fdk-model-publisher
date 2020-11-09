"""Service layer module for modelldcat-ap-no compliant information models from data service descriptions."""
from typing import Optional

from rdflib import Graph
from fdk_rdf_parser import parse_data_services


def is_ready(accept_header: Optional[str]) -> bool:
    """Check if resource is available."""
    if accept_header == "application/json":
        return False
    else:
        return True


def create_information_model():
    pass


def create_rdf_catalog(data_services_rdf):
    data_services = parse_data_services(data_services_rdf)
    for name, service in data_services.items():
        print(f"{name}: {service.endpointDescription}")


