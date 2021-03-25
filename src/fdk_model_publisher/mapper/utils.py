"""Model Element mapping utilities."""

from typing import Any, List, Optional


def build_identifier(title: Optional[str], uri: str, path: List[str]) -> str:
    """Build identifier string."""
    if path and len(path) > 1 and title:
        path_string = "/".join(path[:-1])
        return f"{uri}/{path_string}#{title}"
    elif title:
        return f"{uri}#{title}"
    else:
        return ""


def nested_get(dct: dict, *keys: str) -> Optional[Any]:
    """Multi-level get helper function."""
    for key in keys:
        dct = dct.get(key, {})
    return dct if dct else None


def extract_ref_uri(ref: str, uri: str) -> str:
    """Extract uri from ref."""
    if ref.startswith("#/components/schemas/"):
        return f"{uri}#{ref[21:]}"
    else:
        return f"{uri}#{ref}"


def extract_ref_item(ref_string: str, root_model: dict) -> dict:
    """Extract properties from ref link."""
    path = ref_string[2:].split("/") if ref_string.startswith("#/") else []
    ref_item = nested_get(root_model, *path)
    if len(path) > 0 and ref_item:
        return {"title": path[-1], "properties": ref_item, "path": path[2:-1]}

    return {"title": None, "properties": {}, "path": []}


def extract_type(properties: dict, root_dict: dict) -> str:
    """Extract type from property dictionary."""
    prop_type = properties.get("type", "")
    prop_keys = properties.keys()
    if "allOf" in prop_keys:
        return "allOf"
    elif "$ref" in prop_keys:
        ref_item = extract_ref_item(properties.get("$ref", ""), root_dict)
        ref_type = extract_type(ref_item.get("properties", {}), root_dict)
        if ref_type == "object":
            return "role"
        return ref_type
    elif "enum" in prop_keys:
        return "codeList"
    else:
        return prop_type


def extract_simple_type_restrictions(properties: dict) -> dict:
    """Extract Simple Type restrictions."""
    restrictions = {}
    keys = [
        "minLength",
        "maxLength",
        "pattern",
        "minimum",
        "maximum",
        "length",
        "totalDigits",
        "fractionDigits",
    ]

    for key in keys:
        value = properties.get(key)
        if value is not None:
            restrictions[key] = value

    return restrictions
