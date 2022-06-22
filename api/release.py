#!/usr/bin/env python3
"""
Fred API for Release Namespace.
"""
from api.fred_client import FredClient


class FredAPIRelease(FredClient):
    """Fred API Release Namespace."""

    def get_releases(self, **kwargs) -> dict:
        """Get releases."""
        return self._get(f"releases", {
            **kwargs,
        })

    def get_release(self, release_id: str = None, **kwargs) -> dict:
        """Get release by ID."""
        return self._get(f"release", {
            "release_id": release_id,
            **kwargs,
        })

    def get_release_series(self, release_id: str = None, **kwargs) -> dict:
        """Get release series by ID."""
        return self._get(f"release/series", {
            "release_id": release_id,
            **kwargs,
        })
