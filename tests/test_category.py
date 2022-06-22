#!/usr/bin/env python3
"""
Test the Fred API Category Namespace.
"""
import unittest

import config
from src.fredpy.api import FredAPICategory


class TestFredAPICategory(unittest.TestCase):
    """Test the Fred API Category Namespace."""

    def setUp(self):
        """Setup the test."""
        self.fred_api_category = FredAPICategory(config.API_KEY)

    def test_init_assertion_error(self):
        """Test the init assertion error."""
        with self.assertRaises(AssertionError):
            FredAPICategory()

    def test_get_category(self):
        """Test the get_category method."""
        category_id = 125
        category = self.fred_api_category.get_category(category_id)
        self.assertEqual(category["category_id"], category_id)

    def test_get_category_series(self):
        """Test the get_category_series method."""
        category_id = "1"
        category_series = self.fred_api_category.get_category_series(category_id)
        self.assertEqual(category_series["category_id"], category_id)
