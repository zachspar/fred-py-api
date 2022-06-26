#!/usr/bin/env python3
"""
FRED CLI - Sources Namespace.
"""
import click

from ..api import FredAPISources


@click.command()
@click.pass_context
def sources(ctx):
    """
    Sources namespace API.
    """
    pass
