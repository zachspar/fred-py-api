#!/usr/bin/env python3
"""
Fred API for Category Namespace.
"""
from .fred_client import FredClient


class FredAPICategory(FredClient):
    """Fred API Category Namespace."""

    def get_category(self, category_id: int = None, **kwargs) -> dict:
        """Get category by ID."""
        return self._get(f"category", {
            "category_id": category_id,
            **kwargs,
        })

    def get_category_series(self, category_id: str = None, **kwargs) -> dict:
        """Get category series by ID."""
        return self._get(f"category/series", {
            "category_id": category_id,
            **kwargs,
        })
