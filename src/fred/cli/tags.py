#!/usr/bin/env python3
"""
FRED CLI - Tags Namespace.
"""
import json

import click

from .. import BaseFredAPIError
from .._util import generate_api_kwargs


__all__ = [
    "tags",
]


@click.group()
@click.pass_context
def tags(ctx):
    """
    Tags CLI Namespace.
    """
    pass


@tags.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_tags(ctx, args: tuple):
    """
    Get tags.
    """
    try:
        click.echo(json.dumps(ctx.obj["client"].get_tags(**generate_api_kwargs(args)), indent=4))
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@tags.command()
@click.option("--tag-names", "-t", required=True, type=click.STRING, help="Tag Names.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_related_tags(ctx, tag_names: str, args: tuple):
    """
    Get related tags.
    """
    try:
        click.echo(json.dumps(ctx.obj["client"].get_related_tags(tag_names, **generate_api_kwargs(args)), indent=4))
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@tags.command()
@click.option("--tag-names", "-t", required=True, type=click.STRING, help="Tag Names.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_tags_series(ctx, tag_names: str, args: tuple):
    """
    Get tag series.
    """
    try:
        click.echo(json.dumps(ctx.obj["client"].get_tags_series(tag_names, **generate_api_kwargs(args)), indent=4))
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))