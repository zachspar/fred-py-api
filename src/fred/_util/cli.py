#!/usr/bin/env python3
"""
FRED CLI Utilities.
"""
from json import dumps
from typing import Union, Callable
from xml.etree import ElementTree as ET

import click


__all__ = [
    "generate_api_kwargs",
    "serialize",
    "run_cli_callable",
    "init_cli_context",
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


def serialize(response_obj: Union[dict, ET.Element]) -> str:
    """Serialize a FRED response object to a string."""
    if isinstance(response_obj, dict):
        return dumps(response_obj, indent=4)
    elif isinstance(response_obj, ET.Element):
        return ET.tostring(response_obj, encoding="unicode", method="xml")
    else:
        raise TypeError("response_obj must be a dict or xml.etree.ElementTree.Element")


def run_cli_callable(cli_callable: Callable) -> None:
    """
    Run a CLI callable.
    """
    try:
        cli_callable(auto_envvar_prefix="FRED")
    except AssertionError:
        click.echo(click.style("Error: FRED_API_KEY is not set!", fg="red"))


def init_cli_context(ctx: click.Context, api_key: str, api_client_class: Callable) -> None:
    """
    Initialize a CLI context.
    """
    ctx.ensure_object(dict)

    if "api_key" not in ctx.obj:
        ctx.obj["api_key"] = api_key

    if "client" not in ctx.obj:
        ctx.obj["client"] = api_client_class(api_key=api_key)
