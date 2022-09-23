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
                "command": [
                    "get-series-search",
                    "--search-text",
                    "federal",
                ],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/series/search",
                        params={"series_id": "dff", **self.base_params},
                    ).json(),
                },
            },
        ]
        self.run_test_cases(series, tests)
