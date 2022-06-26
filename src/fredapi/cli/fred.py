#!/usr/bin/env python3
"""
FRED Command Line Interface.
"""
import os

import click


@click.group()
@click.pass_context
def cli(ctx):
    """A fully-featured FRED CLI."""
    ctx.obj = {'api_key': os.environ.get('FRED_API_KEY', None)}
    if not ctx.obj['api_key']:
        raise click.ClickException('FRED_API_KEY environment variable not set.')
