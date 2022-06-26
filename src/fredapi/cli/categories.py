#!/usr/bin/env python3
"""
FRED CLI - Categories Namespace.
"""
import click

from ..api import FredAPICategories


@click.command()
@click.pass_context
def categories(ctx):
    """
    Categories namespace API.
    """
    pass
