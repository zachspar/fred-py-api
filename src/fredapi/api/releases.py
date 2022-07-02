#!/usr/bin/env python3
"""
Fred API for Releases Namespace.
"""
from .fred_client import FredClient
from ..util.decorators import validate_api_args


class FredAPIReleases(FredClient):
    """
    Fred API Releases Namespace.

    Endpoints:
        fred/releases - Get all releases of economic data.
        fred/releases/dates - Get release dates for all releases of economic data.
        fred/release - Get a release of economic data.
        fred/release/dates - Get release dates for a release of economic data.
        fred/release/series - Get the series on a release of economic data.
        fred/release/sources - Get the sources for a release of economic data.
        fred/release/tags - Get the tags for a release.
        fred/release/related_tags - Get the related tags for a release.
        fred/release/tables - Get the release tables for a given release.
    """

    @validate_api_args(
        "api_key", "file_type", "realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order"
    )
    def get_releases(self, **kwargs) -> dict:
        """Get releases."""
        return self._get(f"releases", {**kwargs, })

    def get_releases_dates(self, **kwargs) -> dict:
        """Get releases dates."""
        return self._get(f"releases/dates", {**kwargs, })

    def get_release(self, release_id: int = None, **kwargs) -> dict:
        """Get release by ID."""
        return self._get(f"release", {"release_id": release_id, **kwargs, })

    def get_release_dates(self, release_id: int = None, **kwargs) -> dict:
        """Get release dates by ID."""
        return self._get(f"release/dates", {"release_id": release_id, **kwargs, })

    def get_release_series(self, release_id: int = None, **kwargs) -> dict:
        """Get release series by ID."""
        return self._get(f"release/series", {"release_id": release_id, **kwargs, })

    def get_release_sources(self, release_id: int = None, **kwargs) -> dict:
        """Get release sources by ID."""
        return self._get(f"release/sources", {"release_id": release_id, **kwargs, })

    def get_release_tags(self, release_id: int = None, **kwargs) -> dict:
        """Get release tags by ID."""
        raise NotImplementedError("get_release_tags endpoint is not yet implemented.")

    def get_release_related_tags(self, release_id: int = None, **kwargs) -> dict:
        """Get release related tags by ID."""
        raise NotImplementedError("get_release_related_tags endpoint is not yet implemented.")

    def get_release_tables(self, release_id: int = None, element_id: int = None, **kwargs) -> dict:
        """Get release tables by ID."""
        return self._get(f"release/tables", {"release_id": release_id, "element_id": element_id, **kwargs, })
