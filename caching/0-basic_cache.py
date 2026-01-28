#!/usr/bn/env python3
"""
BasicCache module that implements a simple caching system using a dictionary.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that does not implement
    any eviction strategy and has no limit.
    """

    def put(self, key, item):
        """
        Assigns the item to the cache dictionary using the key.
        If key or item is None, do nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key from the cache.
        If key is None or not found, return None.
        """
        return self.cache_data.get(key, None)
