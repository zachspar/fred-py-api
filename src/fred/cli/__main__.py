#!/usr/bin/env python3
import os

from ..api import FredAPI
from . import _fred_cli


if __name__ == "__main__":
    # set API key
    api_key = os.environ.get("FRED_API_KEY", None)
    assert api_key is not None, "FRED_API_KEY environment variable must be set."

    # run cli
    _fred_cli(
        obj={
            "api_key": api_key,
            "client": FredAPI(api_key=api_key),
        }
    )
