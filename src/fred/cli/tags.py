#!/usr/bin/env python3
"""
FRED CLI - Tags Namespace.
"""
import click

from ..api import FredAPITags


@click.command()
@click.pass_context
def tags(ctx):
    """
    Tags namespace API.
    """
    pass
