#!/usr/bin/env python3
"""
Fred API Client.
"""
from http import HTTPStatus
from os import environ

import requests

from .exceptions import FredAPIRequestError


class FredClient(object):
    """Base Fred API."""

    def __init__(self, api_key: str = None, base_client=None):
        """Init client."""
        if not base_client and not api_key:
            api_key = environ.get("FRED_API_KEY", None)

        assert api_key or base_client, "Fred API Client or API Key required to use FredAPI"

        if base_client and isinstance(base_client, FredClient):
            self._api_key = base_client.get_api_key()
        elif api_key and isinstance(api_key, str):
            self._api_key = api_key
        else:
            raise TypeError(f"Invalid init type")

        self.base_url = "https://api.stlouisfed.org/fred"
        self.base_params = {
            "api_key": self._api_key,
            "file_type": "json",
        }

    def get_api_key(self) -> str:
        """Get API key."""
        return self._api_key

    def _get(self, endpoint: str = None, payload: dict = None) -> dict:
        """Invoke client get request."""
        try:
            resp = requests.get(f"{self.base_url}/{endpoint}", params={**self.base_params, **payload})
        except requests.exceptions.RequestException as e:
            raise FredAPIRequestError(f"Error invoking Fred API: {e}", None)
        if resp.status_code != HTTPStatus.OK:
            raise FredAPIRequestError(resp.text, resp.status_code)
        return resp.json()
