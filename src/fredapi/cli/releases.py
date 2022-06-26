#!/usr/bin/env python3
"""
FRED CLI - Releases Namespace.
"""
import click

from ..api import FredAPIReleases


@click.command()
@click.pass_context
def releases(ctx):
    """
    Releases namespace API.
    """
    pass
