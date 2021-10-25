#!/usr/bin/env python3
"""  MRU Caching """


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching """
    def __init__(self):
        """ MRU Caching """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ MRU Caching """
        if key is None or item is None:
            return
        if len(self.keys) >= self.MAX_ITEMS:
            if key not in self.keys:
                print("DISCARD: {}".format(self.keys[0]))
                del self.cache_data[self.keys[0]]
            del self.keys[0]
        self.keys = [key] + self.keys
        self.cache_data[key] = item

    def get(self, key):
        """ MRU Caching """
        if not key or key not in self.cache_data.keys():
            return None
        del self.keys[self.keys.index(key)]
        self.keys = [key] + self.keys
        return self.cache_data[key]
