#!/usr/bin/env python3
"""
FRED CLI - Series Namespace.
"""
import click

from ..api import FredAPISeries


@click.group()
@click.pass_context
def series(ctx):
    """
    Series CLI Namespace.
    """
    pass


@series.command()
def get_series_observations():
    """Get series observations."""
    pass
