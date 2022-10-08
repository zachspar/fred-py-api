#!/usr/bin/env python3
import unittest
from xml.etree import ElementTree as ET

from fred._util import generate_api_kwargs, serialize


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
