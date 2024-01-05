#!/usr/bin/env python3
from tests.cli import BaseCLITest


class TestCLIEntryPoint(BaseCLITest):
    """Test CLI entry point."""

    def test_fred_cli_entry_point_import_and_run(self):
        """Test the CLI entry point imports properly."""
        from fred.cli.__main__ import run_fred_cli

        self.assertIsNotNone(run_fred_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            run_fred_cli()

    def test_fred_cli_init_entrypoint_import_and_run(self):
        """Test the CLI entry point from __init__."""
        from fred.cli import fred_cli

        self.assertIsNotNone(fred_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            fred_cli()

    def test_categories_cli_entry_point_import_and_run(self):
        """Test the CLI entry point imports properly."""
        from fred.cli.categories import run_categories_cli

        self.assertIsNotNone(run_categories_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            run_categories_cli()

    def test_releases_cli_entry_point_import_and_run(self):
        """Test the CLI entry point imports properly."""
        from fred.cli.releases import run_releases_cli

        self.assertIsNotNone(run_releases_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            run_releases_cli()

    def test_series_cli_entry_point_import_and_run(self):
        """Test the CLI entry point imports properly."""
        from fred.cli.series import run_series_cli

        self.assertIsNotNone(run_series_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            run_series_cli()

    def test_sources_cli_entry_point_import_and_run(self):
        """Test the CLI entry point imports properly."""
        from fred.cli.sources import run_sources_cli

        self.assertIsNotNone(run_sources_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            run_sources_cli()

    def test_tags_cli_entry_point_import_and_run(self):
        """Test the CLI entry point imports properly."""
        from fred.cli.tags import run_tags_cli

        self.assertIsNotNone(run_tags_cli)

        # make sure CLI exits with sys.exit()
        with self.assertRaises(SystemExit):
            run_tags_cli()
