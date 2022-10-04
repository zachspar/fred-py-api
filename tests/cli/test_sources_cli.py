#!/usr/bin/env python3
from requests import get

from fred.cli.sources import sources
from tests.cli import BaseCLITest


class TestCLISources(BaseCLITest):
    """Test CLI utilities."""

    def test_get_sources(self):
        """CLI test for get-sources."""
        tests = [
            {
                "msg": "Basic get-sources test Ok",
                "exit_code": 0,
                "command": ["get-sources"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/tags/sources",
                        params={**self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-sources test Fail",
                "exit_code": 2,
                "command": ["get-sources", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get-tags-series.",
                },
            },
        ]
        self.run_test_cases(sources, tests)


    def test_get_source(self):
        """CLI test for get-source."""
        tests = [
            {
                "msg": "Basic get-source test Ok",
                "exit_code": 0,
                "command": ["get-source", "-i", "1"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/source",
                        params={"source_id": "1", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-source test Fail",
                "exit_code": 2,
                "command": ["get-source", "-i", "1", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_source.",
                },
            },
        ]
        self.run_test_cases(sources, tests)


    def test_get_source_releases(self):
        """CLI test for get-source-releases."""
        tests = [
            {
                "msg": "Basic get-source-releases test Ok",
                "exit_code": 0,
                "command": ["get-source-releases", "-i", "1"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/source/releases",
                        params={"source_id": "1", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-source-releases test Fail",
                "exit_code": 2,
                "command": ["get-source-releases", "-i", "1", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_source-releases.",
                },
            },
        ]
        self.run_test_cases(sources, tests)


