#!/usr/bin/env python3
"""
FRED CLI - Releases Namespace.
"""
import json

import click

from .. import BaseFredAPIError
from .._util import generate_api_kwargs


__all__ = [
    "releases",
]


@click.group()
@click.pass_context
def releases(ctx):
    """
    Releases CLI Namespace.
    """
    pass


@releases.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_releases(ctx, args: tuple):
    """Get releases."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_releases(**generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@releases.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_releases_dates(ctx, args: tuple):
    """Get a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_releases_dates(**generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@releases.command()
@click.option("--release-id", "-r", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release(ctx, release_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_release(release_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@releases.command()
@click.option("--release-id", "-r", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_dates(ctx, release_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_release_dates(release_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@releases.command()
@click.option("--release-id", "-r", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_series(ctx, release_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_release_series(release_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@releases.command()
@click.option("--release-id", "-r", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_sources(ctx, release_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_release_sources(release_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@releases.command()
@click.option("--release-id", "-r", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_tags(ctx, release_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_release_tags(release_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@releases.command()
@click.option("--release-id", "-r", required=True, type=click.INT, help="Release ID.")
@click.option("--tag-names", "-t", required=True, type=click.STRING, help="Tag Names.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_related_tags(ctx, release_id: int, tag_names: str ,args: tuple):
    """Get a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_release_related_tags(release_id, tag_names, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))


@releases.command()
@click.option("--release-id", "-r", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_tables(ctx, release_id: int, args: tuple):
    """Get a category."""
    try:
        click.echo(
            json.dumps(ctx.obj["client"].get_release_tables(release_id, **generate_api_kwargs(args)), indent=4)
        )
    except (ValueError, BaseFredAPIError) as e:
        click.echo(click.style(e, fg="red"))