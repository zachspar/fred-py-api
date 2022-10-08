#!/usr/bin/env python3
import os
from unittest import TestCase, mock


class BaseAPITest(TestCase):
    """Base API Test Case."""

    def setUp(self) -> None:
        self.patcher = mock.patch.dict(os.environ, {"FRED_API_KEY": os.environ.get("TEST_FRED_API_KEY__API")})
        self.patcher.start()
        self.base_params = {
            "api_key": os.environ.get("FRED_API_KEY"),
            "file_type": "json",
        }
        self.client = None

    def tearDown(self) -> None:
        super().tearDown()
        self.patcher.stop()
