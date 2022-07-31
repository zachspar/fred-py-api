#!/usr/bin/env python3
import os

from click import echo, style

from ..api import FredAPI
from . import fred_cli


if __name__ == "__main__":
    # set API key
    api_key = os.environ.get("FRED_API_KEY", None)
    if api_key is None:
        echo(style("ERROR: FRED_API_KEY environment variable is not set!", fg="red"))
        exit(1)

    # run cli
    fred_cli(
        obj={
            "api_key": api_key,
            "client": FredAPI(api_key=api_key),
        }
    )
