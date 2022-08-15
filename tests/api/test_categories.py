#!/usr/bin/env python3
"""
Test the Fred API Categories Namespace.
"""
import unittest

from requests import get

from fred import FredAPICategories
from tests.const import BASE_FRED_URL


class TestFredAPICategories(unittest.TestCase):
    """Test the Fred API Categories Namespace."""

    def setUp(self):
        """Setup the test."""
        self.client = FredAPICategories()
        self.base_params = {
            "api_key": self.client.get_api_key(),
            "file_type": "json",
        }

    def test_get_category(self):
        """Test the get_category method."""
        category_id = 125
        category_data = self.client.get_category(category_id)
        res = get(f"{BASE_FRED_URL}/category", params={"category_id": category_id, **self.base_params})
        self.assertEqual(res.json(), category_data)

    def test_get_category_children(self):
        """Test the get_category_children method."""
        category_id = 0
        category_children_data = self.client.get_category_children(category_id)
        res = get(f"{BASE_FRED_URL}/category/children", params={"category_id": category_id, **self.base_params})
        self.assertEqual(res.json(), category_children_data)

    def test_get_category_related(self):
        """Test the get_category_related method."""
        category_id = 125
        category_related_data = self.client.get_category_related(category_id)
        res = get(f"{BASE_FRED_URL}/category/related", params={"category_id": category_id, **self.base_params})
        self.assertEqual(res.json(), category_related_data)

    def test_get_category_series(self):
        """Test the get_category_series method."""
        category_id = 125
        category_series_data = self.client.get_category_series(category_id)
        res = get(f"{BASE_FRED_URL}/category/series", params={"category_id": category_id, **self.base_params})
        self.assertEqual(res.json(), category_series_data)

    def test_get_category_tags(self):
        """Test the get_category_tags method."""
        category_id = 125
        category_tags_data = self.client.get_category_tags(category_id)
        res = get(f"{BASE_FRED_URL}/category/tags", params={"category_id": category_id, **self.base_params})
        self.assertEqual(res.json(), category_tags_data)

    def test_get_category_related_tags(self):
        """Test the get_category_related_tags method."""
        category_id = 125
        category_related_tags_data = self.client.get_category_related_tags(category_id, "services;quarterly")
        res = get(
            f"{BASE_FRED_URL}/category/related_tags",
            params={"category_id": category_id, "tag_names": "services;quarterly", **self.base_params},
        )
        self.assertEqual(res.json(), category_related_tags_data)
