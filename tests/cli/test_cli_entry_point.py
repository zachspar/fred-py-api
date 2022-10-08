#!/usr/bin/env python3
import click.exceptions

from tests.cli import BaseCLITest


class TestCLIEntryPoint(BaseCLITest):
    """Test CLI entry point."""

    def test_cli_entry_point(self):
        """Test the CLI entry point."""
        from fred.cli.__main__ import run_cli

        # ensure module runs without error
        self.assertIsNotNone(run_cli)

        with self.assertRaises(SystemExit):
            run_cli()
