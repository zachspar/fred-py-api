#!/usr/bin/env python3
"""
A collection of FredAPI exceptions.
"""


__all__ = [
    "BaseFredAPIError",
    "FredAPIRequestError",
]


class BaseFredAPIError(Exception):
    """Base class for all API errors."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class FredAPIRequestError(BaseFredAPIError):
    """Error raised when a request to the API fails."""

    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

    def __str__(self):
        return f"({self.status_code})  {self.message}"
