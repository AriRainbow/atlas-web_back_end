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
        """Add an item to the cache using LIFO eviction.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to be stored in the cache.

        If key or item is None, the method does nothing.
        If the cache exceeds MAX_ITEMS, the last inserted key is discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            if key in self._stack:
                self._stack.remove(key)
            self._stack.append(key)
            return

        # remember the last key BEFORE inserting
        last_key = self._stack[-1] if self._stack else None

        self.cache_data[key] = item
        self._stack.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if last_key is not None:
                if last_key in  self._stack:
                    self._stack.remove(last_key)
                if last_key in self.cache_data:
                    del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item stored under the given key,
            or None if key is None or not found.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
