#!/usr/bin/env python3
import unittest

from fredapi import FredAPISeries
from requests import get

from tests.const import BASE_FRED_URL


class TestFredAPISeries(unittest.TestCase):
    """Test the Fred API Series Namespace."""

    def setUp(self):
        """Setup the test."""
        self.client = FredAPISeries()
        self.base_params = {
            "api_key": self.client.get_api_key(),
            "file_type": "json",
        }

    def test_get_series(self):
        """Test the get_series method."""
        series_id = "DFF"
        series_data = self.client.get_series(series_id)
        res = get(f"{BASE_FRED_URL}/series", params={"series_id": series_id, **self.base_params})
        self.assertEqual(res.json(), series_data)

    def test_get_series_categories(self):
        """Test the get_series_categories method."""
        series_id = "EXJPUS"
        series_categories_data = self.client.get_series_categories(series_id)
        res = get(f"{BASE_FRED_URL}/series/categories", params={"series_id": series_id, **self.base_params})
        self.assertEqual(res.json(), series_categories_data)

    def test_get_series_observations(self):
        """Test the get_series_observations method."""
        series_id = "GNPCA"
        series_observations_data = self.client.get_series_observations(series_id)
        res = get(f"{BASE_FRED_URL}/series/observations", params={"series_id": series_id, **self.base_params})
        self.assertEqual(res.json(), series_observations_data)

    def test_get_series_release(self):
        """Test the get_series_release method."""
        series_id = "IRA"
        series_release_data = self.client.get_series_release(series_id)
        res = get(f"{BASE_FRED_URL}/series/release", params={"series_id": series_id, **self.base_params})
        self.assertEqual(res.json(), series_release_data)

    def test_get_series_search(self):
        """Test the get_series_search method."""
        search_text = "gold"
        series_search_data = self.client.get_series_search(search_text)
        res = get(f"{BASE_FRED_URL}/series/search", params={"search_text": search_text, **self.base_params})
        self.assertEqual(res.json(), series_search_data)

    def test_get_series_search_tags(self):
        """Test the get_series_search_tags method."""
        search_text = "gold"
        series_search_tags_data = self.client.get_series_search_tags(search_text)
        res = get(f"{BASE_FRED_URL}/series/search/tags", params={"series_search_text": search_text, **self.base_params})
        self.assertEqual(res.json(), series_search_tags_data)

    def test_get_series_search_related_tags(self):
        """Test the get_series_search_related_tags method."""
        search_text = "mortgage+rate"
        tag_names = "30-year;frb"
        series_search_related_tags_data = self.client.get_series_search_related_tags(search_text, tag_names)
        res = get(
            f"{BASE_FRED_URL}/series/search/related_tags",
            params={"series_search_text": search_text, "tag_names": tag_names, **self.base_params},
        )
        self.assertEqual(res.json(), series_search_related_tags_data)

    def test_get_series_tags(self):
        """Test the get_series_tags method."""
        series_id = "DFF"
        series_tags_data = self.client.get_series_tags(series_id)
        res = get(f"{BASE_FRED_URL}/series/tags", params={"series_id": series_id, **self.base_params})
        self.assertEqual(res.json(), series_tags_data)

    def test_get_series_updates(self):
        """Test the get_series_updates method."""
        series_updates_data = self.client.get_series_updates()
        res = get(f"{BASE_FRED_URL}/series/updates", params=self.base_params)
        self.assertEqual(res.json(), series_updates_data)

    def test_get_series_vintagedates(self):
        """Test the get_series_vintagedates method."""
        series_id = "DFF"
        series_vintagedates_data = self.client.get_series_vintagedates(series_id)
        res = get(f"{BASE_FRED_URL}/series/vintagedates", params={"series_id": series_id, **self.base_params})
        self.assertEqual(res.json(), series_vintagedates_data)
