#!/usr/bin/env python3
"""
FRED CLI - Releases Namespace.
"""
import click


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
