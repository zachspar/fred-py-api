#!/usr/bin/env python3
import unittest

import click
from click.testing import CliRunner

from fred.cli.sources import sources


class TestCLISources(unittest.TestCase):
    """Test CLI utilities."""

    def setUp(self):
        self.runner = CliRunner()

    def test_get_sources(self):
        """CLI test for get-sources."""
        tests = [
            {
                "msg": "Basic good test",
                "exit_code": 0,
                "command": ["get-sources"],
            },
            {
                "msg": "Basic fail test",
                "exit_code": 2,
                "command": ["get-sources", "asdf=asdf"],
                "raises": click.UsageError,
            },
        ]

        for case in tests:

            with self.subTest(case["msg"], exit_code=case.get("exit_code", None), command=case.get("command", None)):

                if case.get("raises", None):
                    with self.assertRaises(case["raises"]):
                        result = self.runner.invoke(sources, case.get("command", None))
                else:
                    result = self.runner.invoke(sources, case.get("command", None))

                self.assertEqual(case["exit_code"], result.exit_code)

                if case.get("output", None):
                    self.assertEqual(case["output"], result.output)

