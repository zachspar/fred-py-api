#!/usr/bin/env python3
import unittest

from src.fred._util.decorators import validate_api_args


class TestDecorators(unittest.TestCase):
    """Test utility decorators."""

    def test_validate_api_args(self):
        """Test the validate_api_args decorator."""

        class TestClass:
            @validate_api_args("arg1", "arg2")
            def test_func(self, *args, **kwargs) -> None:
                """Test function."""
                pass

        TestClass().test_func(1, 2, arg1=3, arg2=4)

        with self.assertRaises(ValueError):
            TestClass().test_func(1, 2, arg1=3, arg2=4, arg3=5)

        with self.assertRaises(ValueError):
            TestClass().test_func(arg3=3)
