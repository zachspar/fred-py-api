#!/usr/bin/env python3
"""
FRED CLI - Series Namespace.
"""
import click

from ..api import FredAPISeries


@click.command()
@click.pass_context
def series(ctx):
    """
    Series namespace API.
    """
    pass
