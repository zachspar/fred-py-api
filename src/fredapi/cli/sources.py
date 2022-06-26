#!/usr/bin/env python3
"""
FRED CLI - Sources Namespace.
"""
import click

from ..api import FredAPISources, BaseFredAPIError


@click.group()
@click.pass_context
def sources(ctx):
    """
    Sources namespace API.
    """
    ctx.obj["client"]: FredAPISources = FredAPISources(ctx.obj['api_key'])


@sources.command()
@click.pass_context
def get_sources(ctx):
    """
    Get sources.
    """
    try:
        data = ctx.obj["client"].get_sources()
        click.echo(data)
    except BaseFredAPIError as e:
        click.echo(e)


@sources.command()
@click.argument("source-id", type=click.INT, required=True)
@click.pass_context
def get_source(ctx, source_id):
    """
    Get source by ID.
    """
    try:
        data = ctx.obj["client"].get_source(source_id)
        click.echo(data)
    except BaseFredAPIError as e:
        click.echo(e)


@sources.command()
@click.argument("source-id", type=click.INT, required=True)
@click.pass_context
def get_source_releases(ctx, source_id):
    """
    Get source releases by ID.
    """
    try:
        data = ctx.obj["client"].get_source_releases(source_id)
        click.echo(data)
    except BaseFredAPIError as e:
        click.echo(e)
