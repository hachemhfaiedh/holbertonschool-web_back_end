#!/usr/bin/env python3
""" LIFO Caching """


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching """
    def __init__(self):
        """ LIFO Caching """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ LIFO Caching """
        if key is None or item is None:
            return
        if len(self.keys) >= self.MAX_ITEMS:
            if key not in self.keys:
                print("DISCARD: {}".format(self.keys[-1]))
                del self.cache_data[self.keys[-1]]
            del self.keys[-1]
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ LIFO Caching """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
