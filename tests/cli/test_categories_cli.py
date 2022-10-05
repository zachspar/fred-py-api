#!/usr/bin/env python3
from requests import get

from fred.cli.categories import categories
from tests.cli import BaseCLITest


class TestCLICategories(BaseCLITest):
    def test_get_category(self):
        """CLI test for get-category."""
        tests = [
            {
                "msg": "Basic get-category test Ok",
                "exit_code": 0,
                "command": ["get-category", "-i", "53"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/category",
                        params={"category_id": "125", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-category test Fail",
                "exit_code": 2,
                "command": ["get-category", "-i", "125", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_category.",
                },
            },
        ]
        self.run_test_cases(categories, tests)

    def test_get_category_children(self):
        """CLI test for get-category-children."""
        tests = [
            {
                "msg": "Basic get-category test Ok",
                "exit_code": 0,
                "command": ["get-category-children", "-i", "13"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/category/children",
                        params={"category_id": "13", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-category test Fail",
                "exit_code": 2,
                "command": ["get-category-children", "-i", "13", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_category_children.",
                },
            },
        ]
        self.run_test_cases(categories, tests)

    def test_get_category_related(self):
        """CLI test for get-category-related."""
        tests = [
            {
                "msg": "Basic get-category-related test Ok",
                "exit_code": 0,
                "command": ["get-category-related", "-i", "32073"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/category/related",
                        params={"category_id": "32073", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-category-related test Fail",
                "exit_code": 2,
                "command": ["get-category-related", "-i", "32073", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_category_related.",
                },
            },
        ]
        self.run_test_cases(categories, tests)

    def test_get_category_series(self):
        """CLI test for get-category-series."""
        tests = [
            {
                "msg": "Basic get-category-series test Ok",
                "exit_code": 0,
                "command": ["get-category-series", "-i", "125"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/category/series",
                        params={"category_id": "125", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-category-series test Fail",
                "exit_code": 2,
                "command": ["get-category-series", "-i", "125", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_category_series.",
                },
            },
        ]
        self.run_test_cases(categories, tests)

    def test_get_category_tags(self):
        """CLI test for get-category-tags."""
        tests = [
            {
                "msg": "Basic get-category-tags test Ok",
                "exit_code": 0,
                "command": ["get-category-tags", "-i", "125"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/category/tags",
                        params={"category_id": "125", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-category-tags test Fail",
                "exit_code": 2,
                "command": ["get-category-tags", "-i", "125", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_category_tags.",
                },
            },
        ]
        self.run_test_cases(categories, tests)

    def test_get_category_related_tags(self):
        """CLI test for get-category-related-tags."""
        tests = [
            {
                "msg": "Basic get-category-related-tags test Ok",
                "exit_code": 0,
                "command": ["get-category-related-tags", "-i", "125", "-t", "services;quarterly"],
                "output": {
                    "dict": get(
                        "https://api.stlouisfed.org/fred/category/related_tags",
                        params={"category_id": "125", "tag_names": "services;quarterly", **self.base_params},
                    ).json(),
                },
            },
            {
                "msg": "Basic get-category-related-tags test Fail",
                "exit_code": 2,
                "command": ["get-category-related-tags", "-i", "125", "-t", "services;quarterly", "asdf=asdf"],
                "output": {
                    "contains": "Error: asdf is not a valid argument for get_category_related_tags.",
                },
            },
        ]
        self.run_test_cases(categories, tests)
