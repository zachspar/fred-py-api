#!/usr/bin/env python3
"""
Fred API Sources Namespace.
"""
from ._fred_client import *
from .._util.decorators import validate_api_args


__all__ = [
    "FredAPISources",
]


class FredAPISources(FredClient):
    """
    Fred API Sources Namespace.

    Endpoints:
        fred/sources - Get all sources of economic data. https://fred.stlouisfed.org/docs/api/fred/sources.html
        fred/source - Get a source of economic data. https://fred.stlouisfed.org/docs/api/fred/source.html
        fred/source/releases - Get the releases for a source. https://fred.stlouisfed.org/docs/api/fred/source_releases.html
    """

    @validate_api_args(
        "api_key", "file_type", "realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order"
    )
    def get_sources(self, **kwargs) -> JsonOrXml:
        """Get sources. https://fred.stlouisfed.org/docs/api/fred/sources.html"""
        return self._get(
            f"sources",
            {
                **kwargs,
            },
        )

    @validate_api_args("api_key", "file_type", "source_id", "realtime_start", "realtime_end")
    def get_source(self, source_id: int, **kwargs) -> JsonOrXml:
        """Get source by ID. https://fred.stlouisfed.org/docs/api/fred/source.html"""
        return self._get(
            f"source",
            {
                "source_id": source_id,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "source_id",
        "realtime_start",
        "realtime_end",
        "limit",
        "offset",
        "order_by",
        "sort_order",
    )
    def get_source_releases(self, source_id: int, **kwargs) -> JsonOrXml:
        """Get source releases by source ID. https://fred.stlouisfed.org/docs/api/fred/source_releases.html"""
        return self._get(
            f"source/releases",
            {
                "source_id": source_id,
                **kwargs,
            },
        )
