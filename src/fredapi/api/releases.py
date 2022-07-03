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
        return self._get(f"releases", {**kwargs,})

    @validate_api_args(
        "api_key",
        "file_type",
        "realtime_start",
        "realtime_end",
        "limit",
        "offset",
        "order_by",
        "sort_order",
        "include_release_dates_with_no_data",
    )
    def get_releases_dates(self, **kwargs) -> dict:
        """Get releases dates."""
        return self._get(f"releases/dates", {**kwargs,})

    @validate_api_args("api_key", "release_id", "file_type", "realtime_start", "realtime_end")
    def get_release(self, release_id: int, **kwargs) -> dict:
        """Get release by ID."""
        return self._get(f"release", {"release_id": release_id, **kwargs,})

    @validate_api_args(
        "api_key",
        "release_id",
        "file_type",
        "realtime_start",
        "realtime_end",
        "limit",
        "offset",
        "sort_order",
        "include_release_dates_with_no_data",
    )
    def get_release_dates(self, release_id: int, **kwargs) -> dict:
        """Get release dates by ID."""
        return self._get(f"release/dates", {"release_id": release_id, **kwargs,})

    @validate_api_args(
        "api_key",
        "file_type",
        "release_id",
        "realtime_start",
        "realtime_end",
        "limit",
        "offset",
        "order_by",
        "sort_order",
        "filter_variable",
        "filter_value",
        "tag_names",
        "exclude_tag_names",
    )
    def get_release_series(self, release_id: int, **kwargs) -> dict:
        """Get release series by ID."""
        return self._get(f"release/series", {"release_id": release_id, **kwargs,})

    @validate_api_args("api_key", "file_type", "release_id", "realtime_start", "realtime_end")
    def get_release_sources(self, release_id: int, **kwargs) -> dict:
        """Get release sources by ID."""
        return self._get(f"release/sources", {"release_id": release_id, **kwargs,})

    @validate_api_args(
        "api_key",
        "file_type",
        "release_id",
        "realtime_start",
        "realtime_end",
        "tag_names",
        "tag_group_id",
        "search_text",
        "limit",
        "offset",
        "order_by",
        "sort_order",
    )
    def get_release_tags(self, release_id: int, **kwargs) -> dict:
        """Get release tags by ID."""
        return self._get(f"release/tags", {"release_id": release_id, **kwargs,})

    @validate_api_args(
        "api_key",
        "file_type",
        "release_id",
        "realtime_start",
        "realtime_end",
        "tag_names",
        "exclude_tag_names",
        "tag_group_id",
        "search_text",
        "limit",
        "offset",
        "order_by",
        "sort_order",
    )
    def get_release_related_tags(self, release_id: int, tag_names: str, **kwargs) -> dict:
        """Get release related tags by ID."""
        return self._get(f"release/related_tags", {"release_id": release_id, "tag_names": tag_names, **kwargs,})

    @validate_api_args(
        "api_key", "file_type", "release_id", "element_id", "include_observation_values", "observation_date"
    )
    def get_release_tables(self, release_id: int, element_id: int = None, **kwargs) -> dict:
        """Get release tables by ID."""
        return self._get(f"release/tables", {"release_id": release_id, "element_id": element_id, **kwargs,})
