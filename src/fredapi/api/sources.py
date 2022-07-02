#!/usr/bin/env python3
"""
Fred API Sources Namespace.
"""
from .fred_client import FredClient
from ..util.decorators import validate_api_args


class FredAPISources(FredClient):
    """
    Fred API Sources Namespace.
    
    Endpoints:
        fred/sources - Get all sources of economic data.
        fred/source - Get a source of economic data.
        fred/source/releases - Get the releases for a source.
    """

    @validate_api_args(
        "api_key", "file_type", "realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order"
    )
    def get_sources(self, **kwargs) -> dict:
        """Get sources."""
        return self._get(f"sources", {**kwargs,})

    @validate_api_args("api_key", "file_type", "source_id", "realtime_start", "realtime_end")
    def get_source(self, source_id: int, **kwargs) -> dict:
        """Get source by ID."""
        return self._get(f"source", {"source_id": source_id, **kwargs,})

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
    def get_source_releases(self, source_id: int, **kwargs) -> dict:
        """Get source releases by ID."""
        return self._get(f"source/releases", {"source_id": source_id, **kwargs,})
