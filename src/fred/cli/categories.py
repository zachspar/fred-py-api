#!/usr/bin/env python3
"""
FRED CLI - Categories Namespace.
"""
import json

import click

from .. import BaseFredAPIError
from .._util import generate_api_kwargs


__all__ = [
    "categories",
]


@click.group()
@click.pass_context
def categories(ctx):
    """
    Categories CLI Namespace.
    """
    pass


@categories.command()
@click.option("--category-id", "-c", required=True, type=click.INT, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category(ctx, category_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(json.dumps(ctx.obj["client"].get_category(category_id, **generate_api_kwargs(args)), indent=4))
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@categories.command()
@click.option("--category-id", "-c", required=True, type=click.INT, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_children(ctx, category_id: int, args: tuple):
    """Get the child categories."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_category_children(category_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@categories.command()
@click.option("--category-id", "-c", required=True, type=click.INT, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_related(ctx, category_id: int, args: tuple):
    """Get related categories."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_category_related(category_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@categories.command()
@click.option("--category-id", "-c", required=True, type=click.INT, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_series(ctx, category_id: int, args: tuple):
    """Get series in a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_category_series(category_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@categories.command()
@click.option("--category-id", "-c", required=True, type=click.INT, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_tags(ctx, category_id: int, args: tuple):
    """Get FRED tags for a category."""
    try:
        click.echo(json.dumps(ctx.obj["client"].get_category_tags(category_id, **generate_api_kwargs(args)), indent=4))
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@categories.command()
@click.option("--category-id", "-c", required=True, type=click.INT, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_related_tags(ctx, category_id: int, args: tuple):
    """Get related FRED tags for a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_category_related_tags(category_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))
