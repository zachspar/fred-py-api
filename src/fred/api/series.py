#!/usr/bin/env python3
"""
Fred API Series Namespace.
"""
from ._fred_client import *
from .._util.decorators import validate_api_args


__all__ = [
    "FredAPISeries",
]


class FredAPISeries(FredClient):
    """
    Fred API Series Namespace.

    Endpoints:
        fred/series - Get an economic data series. https://fred.stlouisfed.org/docs/api/fred/series.html
        fred/series/categories - Get the categories for an economic data series. https://fred.stlouisfed.org/docs/api/fred/series_categories.html
        fred/series/observations - Get the observations or data values for an economic data series. https://fred.stlouisfed.org/docs/api/fred/series_observations.html
        fred/series/release - Get the release for an economic data series. https://fred.stlouisfed.org/docs/api/fred/series_release.html
        fred/series/search - Get economic data series that match keywords. https://fred.stlouisfed.org/docs/api/fred/series_search.html
        fred/series/search/tags - Get the tags for a series search. https://fred.stlouisfed.org/docs/api/fred/series_search_tags.html
        fred/series/search/related_tags - Get the related tags for a series search. https://fred.stlouisfed.org/docs/api/fred/series_search_related_tags.html
        fred/series/tags - Get the tags for an economic data series. https://fred.stlouisfed.org/docs/api/fred/series_tags.htmlj
        fred/series/updates - Get economic data series sorted by when observations were updated on the FRED® server. https://fred.stlouisfed.org/docs/api/fred/series_updates.htmlj
        fred/series/vintagedates - Get the dates in history when a series' data values were revised or new data values were released. https://fred.stlouisfed.org/docs/api/fred/series_vintage_dates.html
    """

    @validate_api_args("api_key", "file_type", "series_id", "realtime_start", "realtime_end")
    def get_series_categories(self, series_id: str, **kwargs) -> JsonOrXml:
        """Get series categories by series ID. https://fred.stlouisfed.org/docs/api/fred/series_categories.html"""
        return self._get(
            f"series/categories",
            {
                "series_id": series_id,
                **kwargs,
            },
        )

    @validate_api_args("api_key", "file_type", "series_id", "realtime_start", "realtime_end", "order_by", "sort_order")
    def get_series_tags(self, series_id: str, **kwargs) -> JsonOrXml:
        """Get series tags by series ID. https://fred.stlouisfed.org/docs/api/fred/series_tags.html"""
        return self._get(
            f"series/tags",
            {
                "series_id": series_id,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "search_text",
        "search_type",
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
    def get_series_search(self, search_text: str, search_type: str = "full_text", **kwargs) -> JsonOrXml:
        """Get series search by text. https://fred.stlouisfed.org/docs/api/fred/series_search.html"""
        return self._get(
            f"series/search",
            {
                "search_text": search_text,
                "search_type": search_type,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "series_search_text",
        "realtime_start",
        "realtime_end",
        "tag_names",
        "tag_group_id",
        "tag_search_text",
        "limit",
        "offset",
        "order_by",
        "sort_order",
    )
    def get_series_search_tags(self, series_search_text: str, **kwargs) -> JsonOrXml:
        """Get series search tags by text. https://fred.stlouisfed.org/docs/api/fred/series_search_tags.html"""
        return self._get(
            f"series/search/tags",
            {
                "series_search_text": series_search_text,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "series_search_text",
        "realtime_start",
        "realtime_end",
        "tag_names",
        "exclude_tag_names",
        "tag_group_id",
        "tag_search_text",
        "limit",
        "offset",
        "order_by",
        "sort_order",
    )
    def get_series_search_related_tags(self, series_search_text: str, tag_names: str, **kwargs) -> JsonOrXml:
        """Get series related tags by text. https://fred.stlouisfed.org/docs/api/fred/series_search_related_tags.html"""
        return self._get(
            f"series/search/related_tags",
            {
                "series_search_text": series_search_text,
                "tag_names": tag_names,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "series_id",
        "realtime_start",
        "realtime_end",
        "limit",
        "offset",
        "sort_order",
        "observation_start",
        "observation_end",
        "units",
        "frequency",
        "aggregation_method",
        "output_type",
        "vintage_dates",
    )
    def get_series_observations(self, series_id: str, **kwargs) -> JsonOrXml:
        """Get series observations by series ID. https://fred.stlouisfed.org/docs/api/fred/series_observations.html"""
        return self._get(
            f"series/observations",
            {
                "series_id": series_id,
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
        "filter_value",
        "start_time",
        "end_time",
    )
    def get_series_updates(self, **kwargs) -> JsonOrXml:
        """Get series updates. https://fred.stlouisfed.org/docs/api/fred/series_updates.html"""
        # TODO FIXME: Validate start_time and end_time presence if applicable.
        return self._get(
            f"series/updates",
            {
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key", "file_type", "series_id", "realtime_start", "realtime_end", "limit", "offset", "sort_order"
    )
    def get_series_vintagedates(self, series_id: str, **kwargs) -> JsonOrXml:
        """Get series vintagedates by series ID. https://fred.stlouisfed.org/docs/api/fred/series_vintage_dates.html"""
        return self._get(
            f"series/vintagedates",
            {
                "series_id": series_id,
                **kwargs,
            },
        )

    @validate_api_args("api_key", "file_type", "series_id", "realtime_start", "realtime_end")
    def get_series_release(self, series_id: str, **kwargs) -> JsonOrXml:
        """Get series release by series ID. https://fred.stlouisfed.org/docs/api/fred/series_release.html"""
        return self._get(
            f"series/release",
            {
                "series_id": series_id,
                **kwargs,
            },
        )

    @validate_api_args("api_key", "file_type", "series_id", "realtime_start", "realtime_end")
    def get_series(self, series_id: str, **kwargs) -> JsonOrXml:
        """Get series by ID. https://fred.stlouisfed.org/docs/api/fred/series.html"""
        return self._get(
            f"series",
            {
                "series_id": series_id,
                **kwargs,
            },
        )
