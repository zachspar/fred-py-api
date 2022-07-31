#!/usr/bin/env python3
import unittest

from requests import get

from src.fred import FredAPITags
from tests.const import BASE_FRED_URL


class TestFredAPITags(unittest.TestCase):
    """Test the Fred API Tags Namespace."""

    def setUp(self):
        """Setup the test."""
        self.client = FredAPITags()
        self.base_params = {
            "api_key": self.client.get_api_key(),
            "file_type": "json",
        }

    def test_get_tags(self):
        """Test the get_tags method."""
        tags_data = self.client.get_tags()
        res = get(f"{BASE_FRED_URL}/tags", params=self.base_params)
        self.assertEqual(res.json(), tags_data)

    def test_get_related_tags(self):
        """Test the get_related_tags method."""
        tag_names = "slovenia;food;oecd"
        related_tags_data = self.client.get_related_tags(tag_names)
        res = get(f"{BASE_FRED_URL}/related_tags", params={"tag_names": tag_names, **self.base_params})
        self.assertEqual(res.json(), related_tags_data)

    def test_get_tags_series(self):
        """Test the get_tags_series method."""
        tag_names = "slovenia;food;oecd"
        tags_series_data = self.client.get_tags_series(tag_names)
        res = get(f"{BASE_FRED_URL}/tags/series", params={"tag_names": tag_names, **self.base_params})
        self.assertEqual(res.json(), tags_series_data)
