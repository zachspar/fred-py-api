#!/usr/bin/env python3
"""
FRED CLI - Series Namespace.
"""
import click

from .. import BaseFredAPIError
from .._util import generate_api_kwargs, serialize

__all__ = [
    "series",
]


@click.group()
@click.pass_context
def series(ctx):
    """
    Series CLI Namespace.
    """
    pass


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series(ctx, series_id: str, args: tuple):
    """Get series."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_categories(ctx, series_id: str, args: tuple):
    """Get series categories."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_categories(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_observations(ctx, series_id: str, args: tuple):
    """Get series observations."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_observations(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_release(ctx, series_id: str, args: tuple):
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
def get_series_search(ctx, search_text: str, search_type: str, args: tuple):
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
def get_series_search_tags(ctx, series_search_text: str, args: tuple):
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
def get_series_search_related_tags(ctx, series_search_text: str, tag_names: str, args: tuple):
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
def get_series_tags(ctx, series_id: str, args: tuple):
    """Get series tags."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_tags(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_updates(ctx, args: tuple):
    """Get series updates."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_updates(**generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@series.command()
@click.option("--series-id", "-i", required=True, type=click.STRING, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_vintagedates(ctx, series_id: str, args: tuple):
    """Get series vintage dates."""
    try:
        click.echo(serialize(ctx.obj["client"].get_series_vintagedates(series_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)
