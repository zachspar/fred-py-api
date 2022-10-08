#!/usr/bin/env python3
import os

from requests import get

from fred import FredAPITags
from tests.api import BaseAPITest
from tests.const import BASE_FRED_URL


class TestFredAPITags(BaseAPITest):
    """Test the Fred API Tags Namespace."""

    def setUp(self):
        """Setup the test."""
        super().setUp()
        self.client = FredAPITags(api_key=os.environ.get("FRED_API_KEY"))

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
