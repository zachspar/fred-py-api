#!/usr/bin/env python3
from tests.cli import BaseCLITest


class TestCLIEntryPoint(BaseCLITest):
    """Test CLI entry point."""

    def test_cli_entry_point_import_and_run(self):
        """Test the CLI entry point imports properly."""
        from fred.cli.__main__ import run_fred_cli

        self.assertIsNotNone(run_fred_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            run_fred_cli()
