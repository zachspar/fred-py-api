#!/usr/bin/env python3
from . import fred_cli
from .._util import run_cli_callable


__all__ = [
    "run_fred_cli",
]


def run_fred_cli():
    """Run the CLI."""
    run_cli_callable(cli_callable=fred_cli)


if __name__ == "__main__":
    run_fred_cli()
