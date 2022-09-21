#!/usr/bin/env python3
import os
from unittest import TestCase, mock

from click.exceptions import UsageError
from click.testing import CliRunner

from fred.cli.series import series


class TestCLISeries(TestCase):
    """Test cases for Series CLI."""

    def setUp(self) -> None:
        self.runner = CliRunner()
        self.patcher = mock.patch.dict(os.environ, {"FRED_API_KEY": os.environ.get("TEST_FRED_API_KEY_CLI")})
        self.patcher.start()

    def tearDown(self) -> None:
        super().tearDown()
        self.patcher.stop()

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
                "command": ["get-series", "asdf=asdf"],
                "raises": UsageError,
            },
        ]

        for case in tests:

            case_keys = set(case.keys())
            command = case.get("command", None)
            exit_code = case.get("exit_code", None)

            with self.subTest(case["msg"], exit_code=exit_code, command=command):

                if "raises" in case_keys:
                    with self.assertRaises(case["raises"]):
                        result = self.runner.invoke(series, command)
                else:
                    result = self.runner.invoke(series, command)

                self.assertEqual(case["exit_code"], result.exit_code)

                if "output" in case_keys:
                    self.assertEqual(case["output"], result.output)
