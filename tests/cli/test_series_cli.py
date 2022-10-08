#!/usr/bin/env python3
from requests import get

from fred.cli.series import series
from tests.cli import BaseCLITest


class TestCLISeries(BaseCLITest):
    """Test cases for Series CLI."""

    def test_get_series(self):
        """CLI test for get-series."""
        tests = [
            {
                "msg": "Basic get-series test Ok",
                "exit_code": 0,
                "command": ["get-series", "-i", "dff"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series", params={"series_id": "dff", **self.base_params}
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series test Fail",
                "exit_code": 2,
                "command": ["get-series", "-i", "dff", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series.",
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_observations(self):
        """CLI test for get-series-observations."""
        tests = [
            {
                "msg": "Basic get-series-observations test Ok",
                "exit_code": 0,
                "command": ["get-series-observations", "-i", "dff"],
                "output": {
                    "dict": get(
                        f"https://api.stlouisfed.org/fred/series/observations",
                        params={"series_id": "dff", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-observations test Fail",
                "exit_code": 2,
                "command": ["get-series-observations", "-i", "dff", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_observations.",
                },
            },
            {
                "msg": "Test get-series-observations with limit=1 sort_order=desc Ok",
                "exit_code": 0,
                "command": ["get-series-observations", "-i", "dff", "limit=1", "sort_order=desc"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/observations",
                        params={"series_id": "dff", "limit": 1, "sort_order": "desc", **self.base_params},
                    ).json(),
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_release(self):
        """CLI test for get-series-releases."""
        tests = [
            {
                "msg": "Basic get-series-release test Ok",
                "exit_code": 0,
                "command": ["get-series-release", "-i", "dff"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/release",
                        params={"series_id": "dff", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-release test Fail",
                "exit_code": 2,
                "command": ["get-series-release", "-i", "dff", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_release.",
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_categories(self):
        """CLI test for get-categories."""
        tests = [
            {
                "msg": "Basic get-series-categories test Ok",
                "exit_code": 0,
                "command": ["get-series-categories", "-i", "dff"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/categories",
                        params={"series_id": "dff", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-categories test Fail",
                "exit_code": 2,
                "command": ["get-series-categories", "-i", "dff", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_categories.",
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_search(self):
        """CLI test for get-series-search."""
        tests = [
            {
                "msg": "Basic get-series-search test Ok",
                "exit_code": 0,
                "command": ["get-series-search", "--search-text", "monetary+service+index"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/search",
                        params={"search_text": "monetary+service+index", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-search test Fail",
                "exit_code": 2,
                "command": ["get-series-search", "-t", "monetary+service+index", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_search.",
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_search_tags(self):
        """CLI test for get-series-search-tags."""
        tests = [
            {
                "msg": "Basic get-series-search-tags test Ok",
                "exit_code": 0,
                "command": ["get-series-search-tags", "-t", "monetary+service+index"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/search/tags",
                        params={"series_search_text": "monetary+service+index", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-search-tags test Fail",
                "exit_code": 2,
                "command": ["get-series-search-tags", "-t", "monetary+service+index", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_search_tags.",
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_search_related_tags(self):
        """CLI test for get-series-search-related-tags using series_search_text=mortgage+rate&tag_names=30-year;frb"""
        tests = [
            {
                "msg": "Basic get-series-search-related-tags test Ok",
                "exit_code": 0,
                "command": [
                    "get-series-search-related-tags",
                    "-t",
                    "mortgage+rate",
                    "-n",
                    "30-year;frb",
                ],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/search/related_tags",
                        params={
                            "series_search_text": "mortgage+rate",
                            "tag_names": "30-year;frb",
                            **self.base_params,
                        },
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-search-related-tags test Fail",
                "exit_code": 2,
                "command": [
                    "get-series-search-related-tags",
                    "-t",
                    "mortgage+rate",
                    "-n",
                    "30-year;frb",
                    "asdf=asdf",
                ],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_search_related_tags.",
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_tags(self):
        """CLI test for get-series-tags."""
        tests = [
            {
                "msg": "Basic get-series-tags test Ok",
                "exit_code": 0,
                "command": ["get-series-tags", "-i", "dff"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/tags",
                        params={"series_id": "dff", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-tags test Fail",
                "exit_code": 2,
                "command": ["get-series-tags", "-i", "dff", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_tags.",
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_updates(self):
        """CLI test for get-series-updates."""
        tests = [
            {
                "msg": "Basic get-series-updates test Ok",
                "exit_code": 0,
                "command": ["get-series-updates"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/updates",
                        params=self.base_params,
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-updates test Fail",
                "exit_code": 2,
                "command": ["get-series-updates", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_updates.",
                },
            },
        ]
        self.run_test_cases(series, tests)

    def test_get_series_vintagedates(self):
        """CLI test for get-series-vintagedates."""
        tests = [
            {
                "msg": "Basic get-series-vintagedates test Ok",
                "exit_code": 0,
                "command": ["get-series-vintagedates", "-i", "GNPCA"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/vintagedates",
                        params={"series_id": "GNPCA", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-series-vintagedates test Fail",
                "exit_code": 2,
                "command": ["get-series-vintagedates", "-i", "GNPCA", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_series_vintagedates.",
                },
            },
        ]
        self.run_test_cases(series, tests)
