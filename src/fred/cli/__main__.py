#!/usr/bin/env python3
import click

from . import fred_cli


def run_cli():
    """Run the FRED CLI."""
    try:
        fred_cli(auto_envvar_prefix="FRED")
    except AssertionError:
        click.echo(click.style("Error: FRED_API_KEY is not set!", fg="red"))


if __name__ == "__main__":
    run_cli()
