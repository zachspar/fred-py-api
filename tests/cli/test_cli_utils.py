#!/usr/bin/env python3
import unittest
from typing import Any
from xml.etree import ElementTree as ET

import click

from fred._util import generate_api_kwargs, serialize, run_cli_callable, init_cli_context


class TestCLIUtils(unittest.TestCase):
    """Test CLI utilities."""

    def test_generate_api_kwargs(self):
        """Test the generate_api_kwargs function."""
        arguments = ("arg1=1", "arg2=2")
        api_kwargs = generate_api_kwargs(arguments)
        self.assertEqual(api_kwargs, {"arg1": "1", "arg2": "2"})

        arguments = ("arg1=1", "arg2=2", "arg3-3", "arg4=", "arg5")
        api_kwargs = generate_api_kwargs(arguments)
        self.assertEqual(api_kwargs, {"arg1": "1", "arg2": "2", "arg4": ""})

    def test_serialize_dict(self):
        """Test the serialize function with a dict."""
        response_obj = {"key": "value"}
        self.assertEqual(serialize(response_obj), '{\n    "key": "value"\n}')

    def test_serialize_xml(self):
        """Test the serialize function with an xml.etree.ElementTree.Element."""
        response_obj = ET.Element("root")
        ET.SubElement(response_obj, "child")
        self.assertEqual(serialize(response_obj), "<root><child /></root>")

    def test_serialize_error(self):
        """Test the serialize function with an invalid response object."""
        response_obj = "invalid"
        with self.assertRaises(TypeError):
            serialize(response_obj)

    def test_run_cli_callable(self):
        """Test the run_cli_callable function."""

        def fake_cli_callable(auto_envvar_prefix: Any = None):
            raise AssertionError("Fake Fred API callable.")

        self.assertIsNone(run_cli_callable(fake_cli_callable))

    def test_init_cli_context(self):
        """Test the init_cli_context function."""

        @click.command()
        @click.pass_context
        def fake_cli_command(ctx: click.Context):
            pass

        class FakeAPIClient:
            def __init__(self, api_key: str):
                pass

        ctx = click.Context(command=fake_cli_command)
        api_key = "fake_api_key"
        api_client_class = FakeAPIClient

        init_cli_context(ctx, api_key, api_client_class)

        # check that api_key is identical
        self.assertEqual(ctx.obj["api_key"], api_key)

        # check that context client is of type FakeAPIClient
        self.assertTrue(isinstance(ctx.obj["client"], api_client_class))
