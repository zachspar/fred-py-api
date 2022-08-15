#!/usr/bin/env python3
import unittest

from requests import get

from fred import FredAPIReleases
from tests.const import BASE_FRED_URL


class TestFredAPIReleases(unittest.TestCase):
    """Test Fred API Releases Namespace."""

    def setUp(self) -> None:
        """Setup the test."""
        self.client = FredAPIReleases()
        self.base_params = {
            "api_key": self.client.get_api_key(),
            "file_type": "json",
        }

    def test_get_releases(self):
        """Test the get_releases method."""
        releases_data = self.client.get_releases()
        res = get(f"{BASE_FRED_URL}/releases", params=self.base_params)
        self.assertEqual(res.json(), releases_data)

    def test_get_releases_dates(self):
        """Test the get_releases_dates method."""
        releases_dates_data = self.client.get_releases_dates()
        res = get(f"{BASE_FRED_URL}/releases/dates", params=self.base_params)
        self.assertEqual(res.json(), releases_dates_data)

    def test_get_release(self):
        """Test the get_release method."""
        release_id = 53
        release_data = self.client.get_release(release_id)
        res = get(f"{BASE_FRED_URL}/release", params={"release_id": release_id, **self.base_params})
        self.assertEqual(res.json(), release_data)

    def test_get_release_dates(self):
        """Test the get_release_dates method."""
        release_id = 53
        release_dates_data = self.client.get_release_dates(release_id)
        res = get(f"{BASE_FRED_URL}/release/dates", params={"release_id": release_id, **self.base_params})
        self.assertEqual(res.json(), release_dates_data)

    def test_get_release_series(self):
        """Test the get_release_series method."""
        release_id = 53
        release_series_data = self.client.get_release_series(release_id)
        res = get(f"{BASE_FRED_URL}/release/series", params={"release_id": release_id, **self.base_params})
        self.assertEqual(res.json(), release_series_data)

    def test_get_release_sources(self):
        """Test the get_release_sources method."""
        release_id = 53
        release_sources_data = self.client.get_release_sources(release_id)
        res = get(f"{BASE_FRED_URL}/release/sources", params={"release_id": release_id, **self.base_params})
        self.assertEqual(res.json(), release_sources_data)

    def test_get_release_tags(self):
        """Test the get_release_tags method."""
        release_id = 53
        release_tags_data = self.client.get_release_tags(release_id)
        res = get(f"{BASE_FRED_URL}/release/tags", params={"release_id": release_id, **self.base_params})
        self.assertEqual(res.json(), release_tags_data)

    def test_get_release_related_tags(self):
        """Test the get_release_related_tags method."""
        release_id = 86
        tag_names = "sa;foreign"
        release_related_tags_data = self.client.get_release_related_tags(release_id, tag_names)
        res = get(
            f"{BASE_FRED_URL}/release/related_tags",
            params={"release_id": release_id, "tag_names": tag_names, **self.base_params},
        )
        self.assertEqual(res.json(), release_related_tags_data)

    def test_get_release_tables(self):
        """Test the get_release_tables method."""
        release_id = 53
        release_tables_data = self.client.get_release_tables(release_id)
        res = get(f"{BASE_FRED_URL}/release/tables", params={"release_id": release_id, **self.base_params})
        self.assertEqual(res.json(), release_tables_data)
