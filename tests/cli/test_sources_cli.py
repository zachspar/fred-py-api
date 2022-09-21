#!/usr/bin/env python3
from click.exceptions import UsageError

from fred.cli.sources import sources
from tests.cli import BaseCLITest


class TestCLISources(BaseCLITest):
    """Test CLI utilities."""

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
                "raises": UsageError,
            },
        ]
        self.run_test_cases(sources, tests)
