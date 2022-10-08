#!/usr/bin/env python3
import os
from json import loads
from typing import List, Dict
from unittest import TestCase, mock

from click.testing import CliRunner

from fred import FredAPI


class BaseCLITest(TestCase):
    """Base CLI Test Case."""

    def setUp(self) -> None:
        """Set up."""
        self.runner = CliRunner()
        self.patcher = mock.patch.dict(os.environ, {"FRED_API_KEY": os.environ.get("TEST_FRED_API_KEY__CLI")})
        self.patcher.start()
        self.client = FredAPI(api_key=os.environ.get("FRED_API_KEY"))

        # set basic context object for all cli tests
        self.obj = {
            "api_key": self.client.get_api_key(),
            "client": self.client,
        }

        # set basic params for all requests
        self.base_params = {
            "api_key": self.client.get_api_key(),
            "file_type": "json",
        }

    def tearDown(self) -> None:
        """Clean up."""
        super().tearDown()
        # stop mocking API key
        self.patcher.stop()

    def run_test_cases(self, cli, tests: List[Dict]):
        """Common logic for running a list of CLI test cases."""
        for case in tests:

            case_keys = set(case.keys())
            command = case.get("command", None)
            exit_code = case.get("exit_code", None)

            with self.subTest(case["msg"], exit_code=exit_code, command=command):

                # get cli result
                result = self.runner.invoke(cli, command, obj=self.obj)

                # assert output
                if "output" in case_keys:
                    if isinstance(case["output"], dict):
                        comparison_keys = set(case["output"].keys())
                        if "dict" in comparison_keys:
                            self.assertDictEqual(case["output"]["dict"], loads(result.output))
                        elif "contains" in comparison_keys:
                            self.assertIn(case["output"]["contains"], result.output)
                        else:
                            self.assertEqual(case["output"], result.output)
                    else:
                        self.assertEqual(case["output"], result.output)

                # assert exit code
                self.assertEqual(case["exit_code"], result.exit_code)
