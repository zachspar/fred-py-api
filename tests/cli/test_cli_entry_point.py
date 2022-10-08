#!/usr/bin/env python3
from tests.cli import BaseCLITest


class TestCLIEntryPoint(BaseCLITest):
    """Test CLI entry point."""

    def test_cli_entry_point(self):
        """Test the CLI entry point."""
        from fred.cli.__main__ import run_cli

        self.assertIsNotNone(run_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            run_cli()
