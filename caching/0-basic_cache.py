#!/usr/bn/env python3
"""
BasicCache module that implements a simple caching system using a dictionary.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a caching system with no size limit."""

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to be stored in the cache.

        If key or item is None, the method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The item stored under the given key,
            or None if the key does not exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
