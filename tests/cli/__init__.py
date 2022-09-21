#!/usr/bin/env python3
import os
from typing import List, Dict
from unittest import TestCase, mock

from click.testing import CliRunner

from fred import FredAPI


class BaseCLITest(TestCase):
    """Base CLI Test Case."""

    def setUp(self) -> None:
        self.runner = CliRunner()
        self.patcher = mock.patch.dict(os.environ, {"FRED_API_KEY": os.environ.get("TEST_FRED_API_KEY_CLI")})
        self.patcher.start()
        self.client = FredAPI(api_key=os.environ.get("FRED_API_KEY"))
        self.obj = {
            "api_key": self.client.get_api_key(),
            "client": self.client,
        }

    def tearDown(self) -> None:
        super().tearDown()
        self.patcher.stop()

    def run_test_cases(self, cli, tests: List[Dict]):
        """Common logic for running a list of CLI test cases."""
        for case in tests:

            case_keys = set(case.keys())
            command = case.get("command", None)
            exit_code = case.get("exit_code", None)

            with self.subTest(case["msg"], exit_code=exit_code, command=command):

                if "raises" in case_keys:
                    with self.assertRaises(case["raises"]):
                        result = self.runner.invoke(cli, command, obj=self.obj)
                else:
                    result = self.runner.invoke(cli, command, obj=self.obj)

                self.assertEqual(case["exit_code"], result.exit_code)

                if "output" in case_keys:
                    self.assertEqual(case["output"], result.output)
