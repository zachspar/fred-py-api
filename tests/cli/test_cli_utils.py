#!/usr/bin/env python3
import unittest

from src.fred._util import generate_api_kwargs


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
