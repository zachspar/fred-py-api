#!/usr/bin/env python3
"""
Fred API Client.
"""
from http import HTTPStatus
from typing import Optional, Dict, TypeVar
from xml.etree import ElementTree as ET

import requests

from .exceptions import FredAPIRequestError

__all__ = [
    "FredClient",
    "JsonOrXml",
]


JsonOrXml = TypeVar("JsonOrXml", Dict, ET.Element)


class FredClient(object):
    """Base Fred API."""

    def __init__(self, api_key: str = None, base_client: Optional["FredClient"] = None):
        """Init client."""

        assert api_key or base_client, "Fred API Client or API Key required to use FredAPI"

        if base_client and isinstance(base_client, FredClient):
            self._api_key = base_client.get_api_key()
        elif api_key and isinstance(api_key, str):
            self._api_key = api_key
        else:
            raise TypeError(f"Invalid init type")

        if not self._api_key.isalnum() or len(self._api_key) != 32:
            raise ValueError("Invalid API Key - must be 32 characters in length")

        self.base_url = "https://api.stlouisfed.org/fred"
        self.base_params = {
            "api_key": self._api_key,
            "file_type": "json",
        }

    def get_api_key(self) -> str:
        """Get API key."""
        return self._api_key

    def _get(self, endpoint: str = None, payload: dict = None) -> JsonOrXml:
        """Invoke client get request."""
        if not payload:
            payload = {}
        try:
            resp = requests.get(f"{self.base_url}/{endpoint}", params={**self.base_params, **payload})
        except requests.exceptions.RequestException as e:
            raise FredAPIRequestError(f"Error invoking Fred API: {e}", None)
        if resp.status_code != HTTPStatus.OK:
            raise FredAPIRequestError(resp.text, resp.status_code)

        if payload.get("file_type", "json") == "xml":
            return ET.fromstring(resp.content)
        return resp.json()
