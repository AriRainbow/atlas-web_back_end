#!/usr/bin/env python3
""" 4. MRU caching system """

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache discards the most recently used item
    when the cache exceed MAX_ITEMS.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache and update its usage.
        If the cache is full, discard the most recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove key to update its position
            del self.cache_data[key]

        # MRU discard logic BEFORE adding new item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last insert/used key
            mru_key = next(reversed(self.cache_data))
            self.cache_data.pop(mru_key)
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item  # MRU goes to end

    def get(self, key):
        """
        Retieve item and update its usage.
        If not found, return None.
        """
        if key is None or key not in self.cache_data:
            return None
  
        # Update usage to mark it as most recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
