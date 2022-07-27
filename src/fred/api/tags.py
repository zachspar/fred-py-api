#!/usr/bin/env python3
"""
Fred API Tags Namespace.
"""
from ._fred_client import *
from .._util.decorators import validate_api_args


__all__ = [
    "FredAPITags",
]


class FredAPITags(FredClient):
    """
    Fred API Tags Namespace.

    Endpoints:
        fred/tags - Get all tags, search for tags, or get tags by name. https://fred.stlouisfed.org/docs/api/fred/tags.html
        fred/related_tags - Get the related tags for one or more tags. https://fred.stlouisfed.org/docs/api/fred/related_tags.html
        fred/tags/series - Get the series matching tags. https://fred.stlouisfed.org/docs/api/fred/tags_series.html
    """

    @validate_api_args(
        "api_key",
        "file_type",
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
    def get_tags(self, **kwargs) -> JsonOrXml:
        """Get tags. https://fred.stlouisfed.org/docs/api/fred/tags.html"""
        return self._get(
            f"tags",
            {
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
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
    def get_related_tags(self, tag_names: str, **kwargs) -> JsonOrXml:
        """Get related tags by tag names. https://fred.stlouisfed.org/docs/api/fred/related_tags.html"""
        return self._get(
            f"related_tags",
            {
                "tag_names": tag_names,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "realtime_start",
        "realtime_end",
        "tag_names",
        "exclude_tag_names",
        "limit",
        "offset",
        "order_by",
        "sort_order",
    )
    def get_tags_series(self, tag_names: str, **kwargs) -> JsonOrXml:
        """Get tags series by tag names. https://fred.stlouisfed.org/docs/api/fred/tags_series.html"""
        return self._get(
            f"tags/series",
            {
                "tag_names": tag_names,
                **kwargs,
            },
        )
