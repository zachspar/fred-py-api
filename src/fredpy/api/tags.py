#!/usr/bin/env python3
"""
Fred API Tags Namespace.
"""
from .fred_client import FredClient


class FredAPITags(FredClient):
    """
    Fred API Tags Namespace.
    
    Endpoints:
        fred/tags - Get all tags, search for tags, or get tags by name.
        fred/related_tags - Get the related tags for one or more tags.
        fred/tags/series - Get the series matching tags.
    """

    def get_tags(self, **kwargs) -> dict:
        """Get tags."""
        raise NotImplementedError("get_tags endpoint is not yet implemented.")

    def get_related_tags(self, tag_id: str = None, **kwargs) -> dict:
        """Get related tags by ID."""
        raise NotImplementedError("get_related_tags endpoint is not yet implemented.")

    def get_tags_series(self, **kwargs) -> dict:
        """Get tags series by ID."""
        raise NotImplementedError("get_tags_series endpoint is not yet implemented.")
