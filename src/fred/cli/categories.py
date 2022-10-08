#!/usr/bin/env python3
"""
FRED CLI - Categories Namespace.
"""
import click

from .. import BaseFredAPIError
from .._util import generate_api_kwargs, serialize

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
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category(ctx, category_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_children(ctx, category_id: int, args: tuple):
    """Get the child categories."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category_children(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_related(ctx, category_id: int, args: tuple):
    """Get related categories."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category_related(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_series(ctx, category_id: int, args: tuple):
    """Get series in a category."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category_series(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_tags(ctx, category_id: int, args: tuple):
    """Get FRED tags for a category."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category_tags(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.option("--tag-names", "-t", required=True, type=click.STRING, help="Tag Names.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_related_tags(ctx, category_id: int, tag_names: str, args: tuple):
    """Get related FRED tags for a category."""
    try:
        click.echo(
            serialize(ctx.obj["client"].get_category_related_tags(category_id, tag_names, **generate_api_kwargs(args)))
        )
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)
