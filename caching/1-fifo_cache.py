#!/usr/bin/env python3
""" 1. FIFO caching system """

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that evicts the
    first inserted item once the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """Initialize with an ordered dictionary"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using FIFO eviction.
        If the cache exceeds the limit, discard the oldest item.
        """
        if key is None or item is None:
            return
 
        if key in self.cache_data:
            # Remove it first so re-inserting updates order
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # FIFO = pop the first inserted item
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieve item by key from cache.
        Return None if key is missing or None.
        """
        return self.cache_data.get(key, None)
