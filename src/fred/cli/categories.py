#!/usr/bin/env python3
"""
FRED CLI - Categories Namespace.
"""
import click

from .. import BaseFredAPIError, FredAPICategories
from .._util import generate_api_kwargs, serialize, run_cli_callable, init_cli_context

__all__ = [
    "categories",
    "run_categories_cli",
]


@click.group()
@click.option("--api-key", type=click.STRING, required=False, help="FRED API key.")
@click.version_option(version="1.2.0")
@click.pass_context
def categories(ctx: click.Context, api_key: str):
    """
    Categories CLI Namespace.
    """
    init_cli_context(ctx, api_key, FredAPICategories)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category(ctx: click.Context, category_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_children(ctx: click.Context, category_id: int, args: tuple):
    """Get the child categories."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category_children(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_related(ctx: click.Context, category_id: int, args: tuple):
    """Get related categories."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category_related(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_series(ctx: click.Context, category_id: int, args: tuple):
    """Get series in a category."""
    try:
        click.echo(serialize(ctx.obj["client"].get_category_series(category_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@categories.command()
@click.option("--category-id", "-i", required=True, type=click.STRING, help="Category ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_category_tags(ctx: click.Context, category_id: int, args: tuple):
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
def get_category_related_tags(ctx: click.Context, category_id: int, tag_names: str, args: tuple):
    """Get related FRED tags for a category."""
    try:
        click.echo(
            serialize(ctx.obj["client"].get_category_related_tags(category_id, tag_names, **generate_api_kwargs(args)))
        )
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


def run_categories_cli():
    """Run the CLI for Categories namespace."""
    run_cli_callable(cli_callable=categories)


if __name__ == "__main__":
    run_categories_cli()
