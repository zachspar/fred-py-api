#!/usr/bin/env python3
"""
Fred Python API.
"""
from api.category import FredAPICategory
from api.release import FredAPIRelease
from api.series import FredAPISeries


class FredAPI(FredAPISeries, FredAPIRelease, FredAPICategory):
    """Fred API."""

    pass
