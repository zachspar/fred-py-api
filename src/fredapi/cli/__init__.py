#!/usr/bin/env python3
"""CLI Core."""
from .categories import categories
from .fred import cli
from .releases import releases
from .series import series
from .sources import sources
from .tags import tags


if __name__ == "__main__":
    cli.add_command(categories)
    cli.add_command(releases)
    cli.add_command(series)
    cli.add_command(sources)
    cli.add_command(tags)
    cli()
