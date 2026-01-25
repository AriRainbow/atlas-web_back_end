#!/usr/bin/env python3
"""
FIFOCache module that implements a caching system with a FIFO eviction policy.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a caching system with a FIFO eviction policy."""

    def __init__(self):
        """Initialize the FIFOCache."""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to be stored in the cache.

        If key or item is None, the method does nothing.
        Implements FIFO eviction policy when the cache exceeds MAX_ITEMS.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        self.cache_data[key] = item
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.keys_order.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item stored under the given key,
            or None if the key does not exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
    