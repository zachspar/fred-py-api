#!/usr/bin/env python3
"""
FRED CLI - Categories Namespace.
"""
import click


__all__ = [
    "categories",
]


@click.group(invoke_without_command=True)
@click.pass_context
def categories(ctx):
    """
    Categories CLI Namespace.
    """
    pass
