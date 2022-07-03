#!/usr/bin/env python3
import unittest

from requests import get

from src.fredapi import FredAPISources
from tests.const import BASE_FRED_URL


class TestFredAPISources(unittest.TestCase):
    """Test the Fred API Sources Namespace."""

    def setUp(self):
        """Setup the test."""
        self.client = FredAPISources()
        self.base_params = {
            "api_key": self.client.get_api_key(),
            "file_type": "json",
        }

    def test_get_sources(self):
        """Test the get_sources method."""
        sources_data = self.client.get_sources()
        res = get(f"{BASE_FRED_URL}/sources", params=self.base_params)
        self.assertEqual(res.json(), sources_data)

    def test_get_source(self):
        """Test the get_source method."""
        source_id = 1
        source_data = self.client.get_source(source_id)
        res = get(f"{BASE_FRED_URL}/source", params={"source_id": source_id, **self.base_params})
        self.assertEqual(res.json(), source_data)

    def test_get_source_releases(self):
        """Test the get_source_releases method."""
        source_id = 1
        source_releases_data = self.client.get_source_releases(source_id)
        res = get(f"{BASE_FRED_URL}/source/releases", params={"source_id": 1, **self.base_params})
        self.assertEqual(res.json(), source_releases_data)
