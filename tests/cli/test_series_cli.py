#!/usr/bin/env python3
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
            },
            {
                "msg": "Basic get-series test Fail",
                "exit_code": 2,
                "command": ["get-series", "-i", "dff", "asdf=asdf"],
            },
        ]
        self.run_test_cases(series, tests)
