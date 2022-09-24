#!/usr/bin/env python3
from requests import get

from fred.cli.releases import releases
from tests.cli import BaseCLITest


class TestCLIReleases(BaseCLITest):
    """Test cases for Releases CLI."""

    def test_get_releases(self):
        """CLI test for get-releases."""
        tests = [
            {
                "msg": "Basic get-releases test Ok",
                "exit_code": 0,
                "command": ["get-releases"],
                "output": {
                    "dict": get("https://api.stlouisfed.org/fred/releases", params=self.base_params).json(),
                },
            },
            {
                "msg": "Basic get-releases test Fail",
                "exit_code": 2,
                "command": ["get-releases", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_releases.",
                },
            },
        ]
        self.run_test_cases(releases, tests)

    def test_get_releases_dates(self):
        """CLI test for get-releases-dates."""
        tests = [
            {
                "msg": "Basic get-releases-dates test Ok",
                "exit_code": 0,
                "command": ["get-releases-dates"],
                "output": {
                    "dict": get("https://api.stlouisfed.org/fred/releases/dates", params=self.base_params).json(),
                },
            },
            {
                "msg": "Basic get-releases-dates test Fail",
                "exit_code": 2,
                "command": ["get-releases-dates", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_releases_dates.",
                },
            },
        ]
        self.run_test_cases(releases, tests)

    def test_get_release(self):
        """CLI test for get-release."""
        tests = [
            {
                "msg": "Basic get-release test Ok",
                "exit_code": 0,
                "command": ["get-release", "-i", "53"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/release", params={"release_id": "53", **self.base_params}
                    ).json(),
                },
            },
            {
                "msg": "Basic get-release test Fail",
                "exit_code": 2,
                "command": ["get-release", "-i", "53", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_release.",
                },
            },
        ]
        self.run_test_cases(releases, tests)

    def get_release_dates(self):
        """CLI test for get-release-dates."""
        tests = [
            {
                "msg": "Basic get-release-dates test Ok",
                "exit_code": 0,
                "command": ["get-release-dates", "-i", "53"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/release/dates", params={"release_id": "53", **self.base_params}
                    ).json(),
                },
            },
            {
                "msg": "Basic get-release-dates test Fail",
                "exit_code": 2,
                "command": ["get-release-dates", "-i", "53", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_release_dates.",
                },
            },
        ]
        self.run_test_cases(releases, tests)

    def test_get_release_series(self):
        """CLI test for get-release-series."""
        tests = [
            {
                "msg": "Basic get-release-series test Ok",
                "exit_code": 0,
                "command": ["get-release-series", "-i", "53"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/release/series",
                        params={"release_id": "53", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-release-series test Fail",
                "exit_code": 2,
                "command": ["get-release-series", "-i", "53", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_release_series.",
                },
            },
        ]
        self.run_test_cases(releases, tests)

    def test_get_release_sources(self):
        """CLI test for get-release-sources."""
        tests = [
            {
                "msg": "Basic get-release-sources test Ok",
                "exit_code": 0,
                "command": ["get-release-sources", "-i", "53"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/release/sources",
                        params={"release_id": "53", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-release-sources test Fail",
                "exit_code": 2,
                "command": ["get-release-sources", "-i", "53", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_release_sources.",
                },
            },
        ]
        self.run_test_cases(releases, tests)

    def test_get_release_tags(self):
        """CLI test for get-release-tags."""
        tests = [
            {
                "msg": "Basic get-release-tags test Ok",
                "exit_code": 0,
                "command": ["get-release-tags", "-i", "53"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/release/tags", params={"release_id": "53", **self.base_params}
                    ).json(),
                },
            },
            {
                "msg": "Basic get-release-tags test Fail",
                "exit_code": 2,
                "command": ["get-release-tags", "-i", "53", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_release_tags.",
                },
            },
        ]
        self.run_test_cases(releases, tests)

    def test_get_release_related_tags(self):
        """CLI test for get-release-related-tags."""
        tests = [
            {
                "msg": "Basic get-release-related-tags test Ok",
                "exit_code": 0,
                "command": ["get-release-related-tags", "-i", "86", "-t", "sa;foreign"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/release/related_tags",
                        params={"release_id": "86", "tag_names": "sa;foreign", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-release-related-tags test Fail",
                "exit_code": 2,
                "command": ["get-release-related-tags", "-i", "86", "-t", "sa;foreign", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_release_related_tags.",
                },
            },
        ]
        self.run_test_cases(releases, tests)

    def test_get_release_tables(self):
        """CLI test for get-release-tables."""
        tests = [
            {
                "msg": "Basic get-release-tables test Ok",
                "exit_code": 0,
                "command": ["get-release-tables", "-i", "53", "-e", "12886"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/release/tables",
                        params={"release_id": "53", "element_id": "12886", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-release-tables test Fail",
                "exit_code": 2,
                "command": ["get-release-tables", "-i", "53", "-e", "12886", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_release_tables.",
                },
            },
        ]
        self.run_test_cases(releases, tests)
