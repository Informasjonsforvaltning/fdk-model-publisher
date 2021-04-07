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


def extract_type(properties: dict, root_dict: dict, is_property: bool = False) -> str:
    """Extract type from property dictionary."""
    prop_keys = properties.keys()
    prop_type = extract_type_property(properties)
    if "allOf" in prop_keys:
        return "allOf"
    elif "$ref" in prop_keys:
        ref_item = extract_ref_item(properties.get("$ref", ""), root_dict)
        ref_type = extract_type(ref_item.get("properties", {}), root_dict, is_property)
        if ref_type == "object" and is_property or ref_type == "composition":
            return "role"
        return ref_type
    elif "enum" in prop_keys:
        return prop_type if prop_type and is_property else "codeList"
    elif prop_type == "object" and is_property:
        return "composition"
    elif prop_type:
        return prop_type
    elif "properties" in prop_keys and not is_property:
        return "object"
    else:
        return ""


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


def is_simple_type(properties: dict, is_property: bool = False) -> bool:
    """Check if properties map to simple type model element."""
    is_primitive_type = extract_type_property(properties) in {
        "string",
        "boolean",
        "number",
        "int32",
        "integer",
    }
    return is_primitive_type and not is_property


def extract_type_property(properties: dict) -> Optional[str]:
    """Extract type property and nested type property."""
    if "type" in properties.keys():
        return properties.get("type")
    return nested_get(properties, *["schema", "type"])


def first_upper(title: Optional[str]) -> Optional[str]:
    """Shorthand function for capitalizing first letter in title if title exists."""
    if title:
        return title[0].upper() + title[1:]
    else:
        return None


def should_map(title: Optional[str], properties: dict, is_property: bool) -> bool:
    """Shorthand function for determining whether an item should be mapped."""
    return (
        (title is not None and title != "")
        or is_simple_type(properties, is_property)
        or len([key for key in properties.keys() if key != "type"]) > 0
    )
