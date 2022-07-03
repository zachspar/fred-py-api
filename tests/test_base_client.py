#!/usr/bin/env python3
import os
import unittest

from requests import get

from src.fredapi import FredAPIRequestError, BaseFredAPIError
from src.fredapi.api.fred_client import FredClient


class TestBaseFredClient(unittest.TestCase):
    """Test functionality of base FredClient."""

    @staticmethod
    def _unset_env_var():
        """Unset environment variable."""
        os.environ.pop("FRED_API_KEY", None)

    def _set_env_var(self):
        """Set environment variable."""
        os.environ["FRED_API_KEY"] = self.client.get_api_key()

    def setUp(self) -> None:
        """Setup the test."""
        self.client = FredClient()
        self.base_params = {
            "api_key": self.client.get_api_key(),
            "file_type": "json",
        }

    def test_get_request_ok(self):
        """Test instance method _get function."""
        res = self.client._get("/releases")
        self.assertIsNotNone(res)
        self.assertIsInstance(res, dict)
        real = get("https://api.stlouisfed.org/fred/releases", params=self.base_params)
        self.assertEqual(real.json(), res)

    def test_raises_exception(self):
        """Test request raises exception."""
        with self.assertRaises(FredAPIRequestError) as e:
            self.client._get("/nonexistent")

        self.assertEqual(404, e.exception.status_code)
        self.assertEqual('{"error_code":404,"error_message":"Not Found"}', e.exception.message)
        self.assertEqual('(404)  {"error_code":404,"error_message":"Not Found"}', str(e.exception))
        self.assertEqual(
            '{"error_code":404,"error_message":"Not Found"}', super(type(e.exception), e.exception).__str__()
        )

        with self.assertRaises(BaseFredAPIError) as e:
            self.client._get("/nonexistent")

        self.assertEqual(e.exception.message, '{"error_code":404,"error_message":"Not Found"}')
        self.client.base_url = "htt://asdf.asdf"
        try:
            with self.assertRaises(FredAPIRequestError):
                self.client._get("/nonexistent")
        finally:
            self.client.base_url = "https://api.stlouisfed.org/fred"

    def test_get_api_key(self):
        """Test get_api_key method."""
        self.assertIsNotNone(self.client.get_api_key())
        self._unset_env_var()
        try:
            another_client = FredClient("123456")
            self.assertEqual("123456", another_client.get_api_key())
        finally:
            self._set_env_var()

    def test_init_mechanism(self):
        self._unset_env_var()
        try:
            with self.assertRaises(AssertionError):
                FredClient()
        finally:
            self._set_env_var()

        og_client = FredClient()
        self._unset_env_var()
        try:
            FredClient(base_client=og_client)
            FredClient(og_client.get_api_key())
            with self.assertRaises(AssertionError):
                FredClient()
            with self.assertRaises(TypeError):
                FredClient(12345)
        finally:
            self._set_env_var()
