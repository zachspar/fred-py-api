#!/usr/bin/env python3
"""
Fred API Series Namespace.
"""
from .fred_client import FredClient


class FredAPISeries(FredClient):
    """
    Fred API Series Namespace.
    
    Endpoints:
        fred/sources - Get all sources of economic data.
        fred/source - Get a source of economic data.
        fred/source/releases - Get the releases for a source.
    """

    def get_sources(self, **kwargs) -> dict:
        """Get sources."""
        return self._get(f"sources", {
            **kwargs,
        })

    def get_source(self, source_id: str = None, **kwargs) -> dict:
        """Get source by ID."""
        return self._get(f"source", {
            "source_id": source_id,
            **kwargs,
        })

    def get_source_releases(self, source_id: str = None, **kwargs) -> dict:
        """Get source releases by ID."""
        return self._get(f"source/releases", {
            "source_id": source_id,
            **kwargs,
        })
