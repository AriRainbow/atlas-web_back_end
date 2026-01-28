#!/usr/bin/env python3
"""
LRUCache module that implements a caching system with a LRU eviction policy.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache discards the least recently used item
    when the cache exceeds MAX_ITEMS.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache and update its usage.
        If the cache is full, discard the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update position by removing old entry
            del self.cache_data[key]

        self.cache_data[key] = item  # Add to end - most recent

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # LRU = pop the first
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieve item and update its usage.
        If not found, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark this key as recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
