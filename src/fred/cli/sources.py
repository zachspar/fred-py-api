#!/usr/bin/env python3
"""
FRED CLI - Sources Namespace.
"""
import click

from .._util import generate_api_kwargs, serialize
from ..api import BaseFredAPIError

__all__ = [
    "sources",
]


@click.group()
def sources():
    """
    Sources CLI Namespace.
    """
    pass


@sources.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_sources(ctx, args: tuple):
    """
    Get sources.
    """
    try:
        click.echo(serialize(ctx.obj["client"].get_sources(**generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@sources.command()
@click.option("--source-id", "-i", type=click.INT, required=True, help="Source ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_source(ctx, source_id: int, args: tuple):
    """
    Get source by ID.
    """
    try:
        click.echo(serialize(ctx.obj["client"].get_source(source_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@sources.command()
@click.option("--source-id", "-i", type=click.INT, required=True, help="Source ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_source_releases(ctx, source_id: int, args: tuple):
    """
    Get source releases by ID.
    """
    try:
        click.echo(serialize(ctx.obj["client"].get_source_releases(source_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)
