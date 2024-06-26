#!/usr/bin/env python3
"""
FRED CLI - Series Namespace.
"""
import click

from .. import BaseFredAPIError, FredAPISeries
from .._util import generate_api_kwargs, serialize, run_cli_callable, init_cli_context

__all__ = [
    "series",
    "run_series_cli",
]


@click.group()
@click.option("--api-key", type=click.STRING, required=False, help="FRED API key.")
@click.version_option(version="1.2.0")
@click.pass_context
def series(ctx: click.Context, api_key: str):
    """
    Series CLI Namespace.
    """
    init_cli_context(ctx, api_key, FredAPISeries)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series(ctx: click.Context, series_id: str, args: tuple):
    """Get series."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_categories(ctx: click.Context, series_id: str, args: tuple):
    """Get series categories."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_categories(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_observations(ctx: click.Context, series_id: str, args: tuple):
    """Get series observations."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_observations(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_release(ctx: click.Context, series_id: str, args: tuple):
    """Get series release."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_release(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--search-text", "-t", required=True, type=click.STRING, help="Search text.")
@click.option("--search-type", "-s", required=False, type=click.STRING, help="Search type.", default="full_text")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_search(ctx: click.Context, search_text: str, search_type: str, args: tuple):
    """Get series search."""
    try:
        click.echo(
            serialize(ctx.obj["client"].get_series_search(search_text, search_type, **generate_api_kwargs(args)))
        )
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-search-text", "-t", required=True, type=click.STRING, help="Series search text.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_search_tags(ctx: click.Context, series_search_text: str, args: tuple):
    """Get series search tags."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_search_tags(series_search_text, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-search-text", "-t", required=True, type=click.STRING, help="Series search text.")
@click.option("--tag-names", "-n", required=True, type=click.STRING, help="Tag names.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_search_related_tags(ctx: click.Context, series_search_text: str, tag_names: str, args: tuple):
    """Get series search related tags."""
    try:
        click.echo(
            serialize(
                ctx.obj["client"].get_series_search_related_tags(
                    series_search_text, tag_names, **generate_api_kwargs(args)
                )
            )
        )
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_tags(ctx: click.Context, series_id: str, args: tuple):
    """Get series tags."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_tags(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_updates(ctx: click.Context, args: tuple):
    """Get series updates."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_updates(**generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_vintagedates(ctx: click.Context, series_id: str, args: tuple):
    """Get series vintage dates."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_vintagedates(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


def run_series_cli():
    """
    Run the CLI for the Series Namespace.
    """
    run_cli_callable(cli_callable=series)


if __name__ == "__main__":
    run_series_cli()
