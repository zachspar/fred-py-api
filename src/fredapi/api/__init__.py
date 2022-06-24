#!/usr/bin/env python3
"""
Fred API core.
"""
from .categories import FredAPICategories
from .exceptions import BaseFredAPIError, FredAPIRequestError
from .releases import FredAPIReleases
from .series import FredAPISeries
from .sources import FredAPISources
from .tags import FredAPITags


class FredAPI(FredAPISeries, FredAPIReleases, FredAPICategories, FredAPISources, FredAPITags):
    """
    Fred API.
    https://fred.stlouisfed.org/docs/api/fred/
    """

    pass
