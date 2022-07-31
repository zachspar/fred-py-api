#!/usr/bin/env python3
"""
FRED CLI - Series Namespace.
"""
import json

import click


@click.group(invoke_without_command=True)
def series():
    """
    Series CLI Namespace.
    """
    pass


@series.command()
@click.option("--series-id", "-s", required=True, type=click.STRING, help="Series ID.")
@click.pass_context
def get_series_observations(ctx, series_id: str):
    """Get series observations."""
    click.echo(json.dumps(ctx.obj["client"].get_series_observations(series_id, limit=5), indent=4))
