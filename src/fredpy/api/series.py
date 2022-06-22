#!/usr/bin/env python3
"""
Fred API Series Namespace Requests.
"""
from .fred_client import FredClient


class FredAPISeries(FredClient):
    """Fred API Series Namespace."""

    def get_series_observations(self, series_id: str = None, **kwargs) -> dict:
        """Get series observations by ID."""
        return self._get(f"series/observations", {
            "series_id": series_id,
            **kwargs,
        })

    def get_series_release(self, series_id: str = None, **kwargs) -> dict:
        """Get series release by ID."""
        return self._get(f"series/release", {
            "series_id": series_id,
            **kwargs,
        })

    def get_series(self, series_id: str = None, **kwargs) -> dict:
        """Get series by ID."""
        return self._get(f"series", {
            "series_id": series_id,
            **kwargs,
        })
