#!/usr/bin/env python3
"""
Fred API for Categories Namespace.
"""
from ._fred_client import *
from .._util.decorators import validate_api_args


class FredAPICategories(FredClient):
    """
    Fred API Categories Namespace.

    Endpoints:
        * `fred/category - Get a category <https://fred.stlouisfed.org/docs/api/fred/category.html>`_.
        * `fred/category/children - Get the child categories for a specified parent category <https://fred.stlouisfed.org/docs/api/fred/category_children.html>`_.
        * `fred/category/related - Get the related categories for a category <https://fred.stlouisfed.org/docs/api/fred/category_related.html>`_.
        * `fred/category/series - Get the series in a category <https://fred.stlouisfed.org/docs/api/fred/category_series.html>`_.
        * `fred/category/tags - Get the tags for a category <https://fred.stlouisfed.org/docs/api/fred/category_tags.html>`_.
        * `fred/category/related_tags - Get the related tags for a category <https://fred.stlouisfed.org/docs/api/fred/category_related_tags.html>`_.
    """

    @validate_api_args("api_key", "file_type", "category_id")
    def get_category(self, category_id: int = None, **kwargs) -> JsonOrXml:
        """`Get category by ID <https://fred.stlouisfed.org/docs/api/fred/category.html>`_."""
        return self._get(
            f"category",
            {
                "category_id": category_id,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "category_id",
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
    def get_category_series(self, category_id: int, **kwargs) -> JsonOrXml:
        """`Get category series by category ID <https://fred.stlouisfed.org/docs/api/fred/category_series.html>`_."""
        return self._get(
            f"category/series",
            {
                "category_id": category_id,
                **kwargs,
            },
        )

    @validate_api_args("api_key", "file_type", "category_id", "realtime_start", "realtime_end")
    def get_category_children(self, category_id: int = None, **kwargs) -> JsonOrXml:
        """`Get category children by category ID <https://fred.stlouisfed.org/docs/api/fred/category_children.html>`_."""
        return self._get(
            f"category/children",
            {
                "category_id": category_id,
                **kwargs,
            },
        )

    @validate_api_args("api_key", "file_type", "category_id", "realtime_start", "realtime_end")
    def get_category_related(self, category_id: int, **kwargs) -> JsonOrXml:
        """`Get category related by category ID <https://fred.stlouisfed.org/docs/api/fred/category_related.html>`_."""
        return self._get(
            f"category/related",
            {
                "category_id": category_id,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "category_id",
        "realtime_start",
        "realtime_end",
        "limit",
        "offset",
        "order_by",
        "sort_order",
        "filter_variable",
        "filter_value",
        "tag_names",
        "tag_group_id",
        "search_text",
        "limit",
        "offset",
        "order_by",
        "sort_order",
    )
    def get_category_tags(self, category_id: int, **kwargs) -> JsonOrXml:
        """`Get category tags by category ID <https://fred.stlouisfed.org/docs/api/fred/category_tags.html>`_."""
        return self._get(
            f"category/tags",
            {
                "category_id": category_id,
                **kwargs,
            },
        )

    @validate_api_args(
        "api_key",
        "file_type",
        "category_id",
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
        "tag_group_id",
        "search_text",
        "limit",
        "offset",
        "order_by",
        "sort_order",
    )
    def get_category_related_tags(self, category_id: int, tag_names: str, **kwargs) -> JsonOrXml:
        """`Get category related tags by category ID and tag names <https://fred.stlouisfed.org/docs/api/fred/category_related_tags.html>`_."""
        return self._get(
            f"category/related_tags",
            {
                "category_id": category_id,
                "tag_names": tag_names,
                **kwargs,
            },
        )
