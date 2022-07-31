#!/usr/bin/env python3
"""CLI Core."""
import click

# from .categories import categories
# from .releases import releases
# from .sources import sources
# from .tags import tags
from .series import series


_fred_cli = click.CommandCollection(
    sources=[
        series,
    ]
)


__all__ = [
    "_fred_cli",
]
