#!/usr/bin/env python3
"""
FRED CLI Utilities.
"""


__all__ = [
    "generate_api_kwargs",
]


def generate_api_kwargs(arguments: tuple) -> dict:
    """Generate API keyword arguments from CLI variadic arguments."""
    api_kwargs = {}
    for arg in arguments:
        try:
            api_kwargs[arg.split("=")[0]] = arg.split("=")[1]
        except IndexError:
            pass
    return api_kwargs
