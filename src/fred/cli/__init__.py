#!/usr/bin/env python3
"""CLI Core."""
from click import CommandCollection

from .categories import categories
from .releases import releases
from .series import series
from .sources import sources
from .tags import tags


__all__ = [
    "fred_cli",
]

fred_cli = CommandCollection(
    sources=[
        categories,
        releases,
        series,
        sources,
        tags,
    ]
)
