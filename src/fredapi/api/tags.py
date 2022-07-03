#!/usr/bin/env python3
"""
Fred API Tags Namespace.
"""
from .fred_client import FredClient
from ..util.decorators import validate_api_args


class FredAPITags(FredClient):
    """
    Fred API Tags Namespace.
    
    Endpoints:
        fred/tags - Get all tags, search for tags, or get tags by name.
        fred/related_tags - Get the related tags for one or more tags.
        fred/tags/series - Get the series matching tags.
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
    def get_tags(self, **kwargs) -> dict:
        """Get tags."""
        return self._get(f"tags", {**kwargs,})

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
    def get_related_tags(self, tag_names: str, **kwargs) -> dict:
        """Get related tags by ID."""
        return self._get(f"related_tags", {"tag_names": tag_names, **kwargs,})

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
    def get_tags_series(self, tag_names: str, **kwargs) -> dict:
        """Get tags series by ID."""
        return self._get(f"tags/series", {"tag_names": tag_names, **kwargs,})
