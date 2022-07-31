#!/usr/bin/env python3
"""CLI Core."""
from click import CommandCollection

from .series import series


__all__ = [
    "_fred_cli",
]


_fred_cli = CommandCollection(
    sources=[
        series,
    ]
)
