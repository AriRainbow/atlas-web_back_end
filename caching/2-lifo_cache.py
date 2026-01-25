#!/usr/bin/env python3
"""
LIFOCache module that implements a caching system with a LIFO eviction policy.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a caching system with a LIFO eviction policy."""

    def __init__(self):
        """Initialize the LIFOCache."""
        super().__init__()
        self._stack = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to be stored in the cache.

        If key or item is None, the method does nothing.
        Implements LIFO eviction policy when the cache exceeds MAX_ITEMS.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard_key = self._stack.pop()
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

        self.cache_data[key] = item
        self._stack.append(key)

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
