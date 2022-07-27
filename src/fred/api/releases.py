#!/usr/bin/env python3
"""
Fred API for Releases Namespace.
"""
from ._fred_client import *
from .._util.decorators import validate_api_args


__all__ = [
    "FredAPIReleases",
]


class FredAPIReleases(FredClient):
    """
    Fred API Releases Namespace.

    Endpoints:
        fred/releases - Get all releases of economic data. https://fred.stlouisfed.org/docs/api/fred/releases.html
        fred/releases/dates - Get release dates for all releases of economic data. https://fred.stlouisfed.org/docs/api/fred/releases_dates.html
        fred/release - Get a release of economic data. https://fred.stlouisfed.org/docs/api/fred/release.html
        fred/release/dates - Get release dates for a release of economic data. https://fred.stlouisfed.org/docs/api/fred/release_dates.html
        fred/release/series - Get the series on a release of economic data. https://fred.stlouisfed.org/docs/api/fred/release_series.html
        fred/release/sources - Get the sources for a release of economic data. https://fred.stlouisfed.org/docs/api/fred/release_sources.html
        fred/release/tags - Get the tags for a release. https://fred.stlouisfed.org/docs/api/fred/release_tags.html
        fred/release/related_tags - Get the related tags for a release. https://fred.stlouisfed.org/docs/api/fred/release_related_tags.html
        fred/release/tables - Get the release tables for a given release. https://fred.stlouisfed.org/docs/api/fred/release_tables.html
    """

    @validate_api_args(
        "api_key", "file_type", "realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order"
    )
    def get_releases(self, **kwargs) -> JsonOrXml:
        """Get releases. https://fred.stlouisfed.org/docs/api/fred/releases.html"""
        return self._get(
            f"releases",
            {
                **kwargs,
            },
        )

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
    def get_releases_dates(self, **kwargs) -> JsonOrXml:
        """Get releases dates. https://fred.stlouisfed.org/docs/api/fred/releases_dates.html"""
        return self._get(
            f"releases/dates",
            {
                **kwargs,
            },
        )

    @validate_api_args("api_key", "release_id", "file_type", "realtime_start", "realtime_end")
    def get_release(self, release_id: int, **kwargs) -> JsonOrXml:
        """Get release by ID. https://fred.stlouisfed.org/docs/api/fred/release.html"""
        return self._get(
            f"release",
            {
                "release_id": release_id,
                **kwargs,
            },
        )

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
    def get_release_dates(self, release_id: int, **kwargs) -> JsonOrXml:
        """Get release dates by release ID. https://fred.stlouisfed.org/docs/api/fred/release_dates.html"""
        return self._get(
            f"release/dates",
            {
                "release_id": release_id,
                **kwargs,
            },
        )

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
    def get_release_series(self, release_id: int, **kwargs) -> JsonOrXml:
        """Get release series by release ID. https://fred.stlouisfed.org/docs/api/fred/release_series.html"""
        return self._get(
            f"release/series",
            {
                "release_id": release_id,
                **kwargs,
            },
        )

    @validate_api_args("api_key", "file_type", "release_id", "realtime_start", "realtime_end")
    def get_release_sources(self, release_id: int, **kwargs) -> JsonOrXml:
        """Get release sources by release ID. https://fred.stlouisfed.org/docs/api/fred/release_sources.html"""
        return self._get(
            f"release/sources",
            {
                "release_id": release_id,
                **kwargs,
            },
        )

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
    def get_release_tags(self, release_id: int, **kwargs) -> JsonOrXml:
        """Get release tags by release ID. https://fred.stlouisfed.org/docs/api/fred/release_tags.html"""
        return self._get(
            f"release/tags",
            {
                "release_id": release_id,
                **kwargs,
            },
        )

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
    def get_release_related_tags(self, release_id: int, tag_names: str, **kwargs) -> JsonOrXml:
        """Get release related tags by release ID and tag names.
        https://fred.stlouisfed.org/docs/api/fred/release_related_tags.html"""
        return self._get(
            f"release/related_tags",
            {
                "release_id": release_id,
                "tag_names": tag_names,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key", "file_type", "release_id", "element_id", "include_observation_values", "observation_date"
    )
    def get_release_tables(self, release_id: int, element_id: int = None, **kwargs) -> JsonOrXml:
        """Get release tables by release ID and element ID.
        https://fred.stlouisfed.org/docs/api/fred/release_tables.html"""
        return self._get(
            f"release/tables",
            {
                "release_id": release_id,
                "element_id": element_id,
                **kwargs,
            },
        )
