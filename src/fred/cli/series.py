#!/usr/bin/env python3
"""
FRED CLI - Series Namespace.
"""
import json

import click

from .. import BaseFredAPIError
from .._util import generate_api_kwargs


__all__ = [
    "series",
]


@click.group()
def series():
    """
    Series CLI Namespace.
    """
    pass



@series.command()
@click.option("--series-id", "-s", required=True, type=click.INT, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series(ctx, series_id: int, args: tuple):
    """Get series."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series(series_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@series.command()
@click.option("--series-id", "-s", required=True, type=click.INT, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_categories(ctx, series_id: int, args: tuple):
    """Get series categories."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_categories(series_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))



@series.command()
@click.option("--series-id", "-s", required=True, type=click.INT, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_observations(ctx, series_id: int, args: tuple):
    """Get series observations."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_observations(series_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))

@series.command()
@click.option("--series-id", "-s", required=True, type=click.INT, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_release(ctx, series_id: int, args: tuple):
    """Get series release."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_release(series_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@series.command()
@click.option("--search-text", "-s", required=True, type=click.STRING, help="Search text.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_search(ctx, search_text: str, args: tuple):
    """Get series search."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_search(search_text, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))



@series.command()
@click.option("--series-search-text", "-s", required=True, type=click.STRING, help="Series search text.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_search_tags(ctx, series_search_text: str, args: tuple):
    """Get series search tags."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_search_tags(series_search_text, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@series.command()
@click.option("--series-search-text", "-s", required=True, type=click.STRING, help="Series search text.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_search_related_tags(ctx, series_search_text: str, args: tuple):
    """Get series search related tags."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_search_related_tags(series_search_text, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@series.command()
@click.option("--series-id", "-s", required=True, type=click.INT, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_tags(ctx, series_id: int, args: tuple):
    """Get series tags."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_tags(series_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@series.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_updates(ctx, args: tuple):
    """Get series updates."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_updates(**generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@series.command()
@click.option("--series-id", "-s", required=True, type=click.INT, help="Series ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_series_vintagedates(ctx, series_id: int, args: tuple):
    """Get series vintage dates."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_series_vintagedates(series_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


