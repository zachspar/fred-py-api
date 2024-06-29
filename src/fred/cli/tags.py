#!/usr/bin/env python3
"""
FRED CLI - Tags Namespace.
"""
import click

from .. import BaseFredAPIError, FredAPITags
from .._util import generate_api_kwargs, serialize, run_cli_callable, init_cli_context

__all__ = [
    "tags",
    "run_tags_cli",
]


@click.group()
@click.option("--api-key", type=click.STRING, required=False, help="FRED API key.")
@click.version_option(version="1.2.0")
@click.pass_context
def tags(ctx: click.Context, api_key: str):
    """
    Tags CLI Namespace.
    """
    init_cli_context(ctx, api_key, FredAPITags)


@tags.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_tags(ctx: click.Context, args: tuple):
    """
    Get tags.
    """
    try:
        click.echo(serialize(ctx.obj["client"].get_tags(**generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@tags.command()
@click.option("--tag-names", "-t", required=True, type=click.STRING, help="Tag Names.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_related_tags(ctx: click.Context, tag_names: str, args: tuple):
    """
    Get related tags.
    """
    try:
        click.echo(serialize(ctx.obj["client"].get_related_tags(tag_names, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@tags.command()
@click.option("--tag-names", "-t", required=True, type=click.STRING, help="Tag Names.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_tags_series(ctx: click.Context, tag_names: str, args: tuple):
    """
    Get tag series.
    """
    try:
        click.echo(serialize(ctx.obj["client"].get_tags_series(tag_names, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


def run_tags_cli():
    """Run the CLI for Tags namespace."""
    run_cli_callable(cli_callable=tags)


if __name__ == "__main__":
    run_tags_cli()
