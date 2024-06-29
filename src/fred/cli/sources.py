#!/usr/bin/env python3
"""
FRED CLI - Sources Namespace.
"""
import click

from ..api import BaseFredAPIError, FredAPISources
from .._util import generate_api_kwargs, serialize, run_cli_callable, init_cli_context

__all__ = [
    "sources",
    "run_sources_cli",
]


@click.group()
@click.option("--api-key", type=click.STRING, required=False, help="FRED API key.")
@click.version_option(version="1.2.0")
@click.pass_context
def sources(ctx: click.Context, api_key: str):
    """
    Sources CLI Namespace.
    """
    init_cli_context(ctx, api_key, FredAPISources)


@sources.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_sources(ctx: click.Context, args: tuple):
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
def get_source(ctx: click.Context, source_id: int, args: tuple):
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
def get_source_releases(ctx: click.Context, source_id: int, args: tuple):
    """
    Get source releases by ID.
    """
    try:
        click.echo(serialize(ctx.obj["client"].get_source_releases(source_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


def run_sources_cli():
    """
    Run the CLI for the Sources namespace.
    """
    run_cli_callable(cli_callable=sources)


if __name__ == "__main__":
    run_sources_cli()
