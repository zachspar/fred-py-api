#!/usr/bin/env python3
"""
Fred Python API.
"""
from .category import FredAPICategory
from .release import FredAPIRelease
from .series import FredAPISeries


class FredAPI(FredAPISeries, FredAPIRelease, FredAPICategory):
    """Fred API."""

    pass
