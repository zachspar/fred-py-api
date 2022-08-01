#!/usr/bin/env python3
"""
FRED API Decorators.
"""
from functools import wraps


__all__ = [
    "validate_api_args",
]


def validate_api_args(*valid_args):
    """Class method decorator to validate API arguments."""

    def decorator(method):
        """Validate API arguments."""

        @wraps(method)
        def inner(self, *method_args, **method_kwargs):
            for arg, val in method_kwargs.items():
                if arg not in valid_args:
                    raise ValueError(f"{arg} is not a valid argument for {method.__name__}.")
            return method(self, *method_args, **method_kwargs)

        return inner

    return decorator
