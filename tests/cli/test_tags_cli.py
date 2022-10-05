#!/usr/bin/env python3
from requests import get

from fred.cli.tags import tags
from tests.cli import BaseCLITest


class TestCLITags(BaseCLITest):
    def test_get_tags(self):
        """CLI test for get-tags."""
        tests = [
            {
                "msg": "Basic get-tags test Ok",
                "exit_code": 0,
                "command": ["get-tags"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/tags",
                        params={**self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-tags test Fail",
                "exit_code": 2,
                "command": ["get-tags", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_tags.",
                },
            },
        ]
        self.run_test_cases(tags, tests)

    def test_get_related_tags(self):
        """CLI test for get-related-tags."""
        tests = [
            {
                "msg": "Basic get-related-tags test Ok",
                "exit_code": 0,
                "command": ["get-related-tags", "-t", "monetary+aggregates;weekly"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/related_tags",
                        params={"tag_names": "monetary+aggregates;weekly", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-related_tags test Fail",
                "exit_code": 2,
                "command": ["get-related-tags", "-t", "monetary+aggregates;weekly", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_related_tags.",
                },
            },
        ]
        self.run_test_cases(tags, tests)

    def test_get_tags_series(self):
        """CLI test for get-tags-series."""
        tests = [
            {
                "msg": "Basic get-tags-series test Ok",
                "exit_code": 0,
                "command": ["get-tags-series", "-t", "monetary+aggregates;weekly"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/tags/series",
                        params={"tag_names": "monetary+aggregates;weekly", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-tags-series test Fail",
                "exit_code": 2,
                "command": ["get-tags-series", "-t", "monetary+aggregates;weekly", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get-tags-series.",
                },
            },
        ]
        self.run_test_cases(tags, tests)
