#!/usr/bin/env python3
"""
Fred API Series Namespace Requests.
"""
from .fred_client import FredClient


class FredAPISeries(FredClient):
    """
    Fred API Series Namespace.

    Endpoints:
        fred/series - Get an economic data series.
        fred/series/categories - Get the categories for an economic data series.
        fred/series/observations - Get the observations or data values for an economic data series.
        fred/series/release - Get the release for an economic data series.
        fred/series/search - Get economic data series that match keywords.
        fred/series/search/tags - Get the tags for a series search.
        fred/series/search/related_tags - Get the related tags for a series search.
        fred/series/tags - Get the tags for an economic data series.
        fred/series/updates - Get economic data series sorted by when observations were updated on the FRED® server.
        fred/series/vintagedates - Get the dates in history when a series' data values were revised or new data values were released.
    """

    def get_series_categories(self, series_id: str = None, **kwargs) -> dict:
        """Get series categories by ID."""
        return self._get(f"series/categories", {"series_id": series_id, **kwargs, })

    def get_series_tags(self, series_id: str = None, **kwargs) -> dict:
        """Get series tags by ID."""
        return self._get(f"series/tags", {"series_id": series_id, **kwargs, })

    def get_series_search(self, search_text: str = None, search_type: str = "full_text", **kwargs) -> dict:
        """Get series search by text."""
        return self._get(f"series/search", {"search_text": search_text, "search_type": search_type, **kwargs, })

    def get_series_search_tags(self, **kwargs) -> dict:
        """Get series search tags by text."""
        raise NotImplementedError("get_series_search_tags endpoint is not yet implemented.")

    def get_series_related_tags(self, **kwargs) -> dict:
        """Get series related tags by text."""
        raise NotImplementedError("get_series_related_tags endpoint is not yet implemented.")

    def get_series_observations(self, series_id: str = None, **kwargs) -> dict:
        """Get series observations by ID."""
        return self._get(f"series/observations", {"series_id": series_id, **kwargs, })

    def get_series_updates(self, **kwargs) -> dict:
        """Get series updates."""
        return self._get(f"series/updates", {**kwargs, })

    def get_series_vintagedates(self, series_id: str = None, **kwargs) -> dict:
        """Get series vintagedates by ID."""
        return self._get(f"series/vintagedates", {"series_id": series_id, **kwargs, })

    def get_series_release(self, series_id: str = None, **kwargs) -> dict:
        """Get series release by ID."""
        return self._get(f"series/release", {"series_id": series_id, **kwargs, })

    def get_series(self, series_id: str = None, **kwargs) -> dict:
        """Get series by ID."""
        return self._get(f"series", {"series_id": series_id, **kwargs, })
