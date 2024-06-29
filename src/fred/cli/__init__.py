#!/usr/bin/env python3
"""CLI Core."""
import click
from click import group

from fred import FredAPI
from .categories import categories as categories_cli_callable
from .releases import releases as releases_cli_callable
from .series import series as series_cli_callable
from .sources import sources as sources_cli_callable
from .tags import tags as tags_cli_callable
from .._util.cli import init_cli_context

__all__ = [
    "fred_cli",
]


@group()
@click.option("--api-key", type=click.STRING, required=False, help="FRED API key.")
@click.version_option(version="1.2.0")
@click.pass_context
def fred_cli(ctx: click.Context, api_key: str):
    """CLI for the Federal Reserve Economic Data (FRED)."""
    init_cli_context(ctx, api_key, FredAPI)


# add each FRED command group
fred_cli.add_command(categories_cli_callable)
fred_cli.add_command(releases_cli_callable)
fred_cli.add_command(series_cli_callable)
fred_cli.add_command(sources_cli_callable)
fred_cli.add_command(tags_cli_callable)
