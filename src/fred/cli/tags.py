#!/usr/bin/env python3
"""
FRED CLI - Tags Namespace.
"""
import click


__all__ = [
    "tags",
]


@click.group()
@click.pass_context
def tags(ctx):
    """
    Tags CLI Namespace.
    """
    pass
