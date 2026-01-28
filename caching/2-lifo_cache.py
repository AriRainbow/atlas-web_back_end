#!/usr/bin/env python3
"""
LIFOCache module that implements a caching system with a LIFO eviction policy.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that evicts the
    most recently added item when the cache exceeds its limit.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.key_stack = []  # List to track insertion order

    def put(self, key, item):
        """
        Add an item usinf LIFO eviction if needed.
        Discard the last inserted item if cache is full.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove key to update its position in stack
            self.key_stack.remove(key)
        self.cache_data[key] = item
        self.key_stack.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # LIFO = pop the last inserted key
            last_key = self.key_stack.pop(-2)  # Remove second-to-last
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Retrieve item by key from cache.
        Return None if key is missing or None.
        """
        return self.cache_data.get(key, None)
