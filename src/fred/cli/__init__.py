#!/usr/bin/env python3
"""CLI Core."""
import click
from click import group

from fred import FredAPI
from .categories import categories
from .releases import releases
from .series import series
from .sources import sources
from .tags import tags

__all__ = [
    "fred_cli",
]


@group()
@click.option("--api-key", type=click.STRING, required=False, help="FRED API key.")
@click.pass_context
def fred_cli(ctx, api_key: str):
    """CLI for the Federal Reserve Economic Data (FRED)."""
    ctx.ensure_object(dict)
    ctx.obj["api_key"] = api_key
    ctx.obj["client"] = FredAPI(api_key=api_key)


# add each FRED command group
fred_cli.add_command(categories)
fred_cli.add_command(releases)
fred_cli.add_command(series)
fred_cli.add_command(sources)
fred_cli.add_command(tags)
