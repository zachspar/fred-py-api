#!/usr/bin/env python3
"""
FRED CLI - Releases Namespace.
"""
import click

from .. import BaseFredAPIError, FredAPIReleases
from .._util import generate_api_kwargs, serialize, run_cli_callable, init_cli_context

__all__ = ["releases", "run_releases_cli"]


@click.group()
@click.option("--api-key", type=click.STRING, required=False, help="FRED API key.")
@click.version_option(version="1.2.0")
@click.pass_context
def releases(ctx: click.Context, api_key: str):
    """
    Releases CLI Namespace.
    """
    init_cli_context(ctx, api_key, FredAPIReleases)


@releases.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_releases(ctx: click.Context, args: tuple):
    """Get all releases of economic data."""
    try:
        click.echo(serialize(ctx.obj["client"].get_releases(**generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@releases.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get_releases_dates(ctx: click.Context, args: tuple):
    """Get release dates for all releases of economic data."""
    try:
        click.echo(serialize(ctx.obj["client"].get_releases_dates(**generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@releases.command()
@click.option("--release-id", "-i", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release(ctx: click.Context, release_id: int, args: tuple):
    """Get a release of economic data."""
    try:
        click.echo(serialize(ctx.obj["client"].get_release(release_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@releases.command()
@click.option("--release-id", "-i", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_dates(ctx: click.Context, release_id: int, args: tuple):
    """Get release dates for a release of economic data."""
    try:
        click.echo(serialize(ctx.obj["client"].get_release_dates(release_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@releases.command()
@click.option("--release-id", "-i", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_series(ctx: click.Context, release_id: int, args: tuple):
    """Get the series on a release of economic data."""
    try:
        click.echo(serialize(ctx.obj["client"].get_release_series(release_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@releases.command()
@click.option("--release-id", "-i", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_sources(ctx: click.Context, release_id: int, args: tuple):
    """Get the sources for a release of economic data."""
    try:
        click.echo(serialize(ctx.obj["client"].get_release_sources(release_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@releases.command()
@click.option("--release-id", "-i", required=True, type=click.INT, help="Release ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_tags(ctx: click.Context, release_id: int, args: tuple):
    """Get the tags for a release."""
    try:
        click.echo(serialize(ctx.obj["client"].get_release_tags(release_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@releases.command()
@click.option("--release-id", "-i", required=True, type=click.INT, help="Release ID.")
@click.option("--tag-names", "-t", required=True, type=click.STRING, help="Tag Names.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_related_tags(ctx: click.Context, release_id: int, tag_names: str, args: tuple):
    """Get the related tags for a release."""
    try:
        click.echo(
            serialize(ctx.obj["client"].get_release_related_tags(release_id, tag_names, **generate_api_kwargs(args)))
        )
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


@releases.command()
@click.option("--release-id", "-i", required=True, type=click.INT, help="Release ID.")
@click.option("--element-id", "-e", required=False, type=click.INT, help="Element ID.")
@click.argument("args", nargs=-1)
@click.pass_context
def get_release_tables(ctx: click.Context, release_id: int, element_id: int, args: tuple):
    """Get the release table for a given release."""
    try:
        click.echo(serialize(ctx.obj["client"].get_release_tables(release_id, element_id, **generate_api_kwargs(args))))
    except (ValueError, BaseFredAPIError) as e:
        raise click.UsageError(click.style(e, fg="red"), ctx)


def run_releases_cli():
    """
    Run the CLI for the Releases namespace.
    """
    run_cli_callable(cli_callable=releases)


if __name__ == "__main__":
    run_releases_cli()
