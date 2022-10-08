#!/usr/bin/env python3
"""
FRED CLI Utilities.
"""
from json import dumps
from typing import Union
from xml.etree import ElementTree as ET


__all__ = [
    "generate_api_kwargs",
    "serialize",
]


def generate_api_kwargs(arguments: tuple) -> dict:
    """Generate API keyword arguments from CLI variadic arguments."""
    api_kwargs = {}
    for arg in arguments:
        try:
            api_kwargs[arg.split("=")[0]] = arg.split("=")[1]
        except IndexError:
            pass
    return api_kwargs


def serialize(response_obj: Union[dict, ET.Element]) -> str:
    """Serialize a FRED response object to a string."""
    if isinstance(response_obj, dict):
        return dumps(response_obj, indent=4)
    elif isinstance(response_obj, ET.Element):
        return ET.tostring(response_obj, encoding="unicode", method="xml")
    else:
        raise TypeError("response_obj must be a dict or xml.etree.ElementTree.Element")
