#!/usr/bin/env python3
"""
FRED CLI - Series Namespace.
"""
import json

import click

from .._util import generate_api_kwargs


__all__ = [
    "series",
]


@click.group(invoke_without_command=True)
def series():
    """
    Series CLI Namespace.
    """
    pass


@series.command()
@click.option("--series-id", "-s", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_observations(ctx, series_id: str, args: tuple):
    """Get series observations."""
    click.echo(json.dumps(ctx.obj["client"].get_series_observations(series_id, **generate_api_kwargs(args)), indent=4))
