#!/usr/bin/env python3
"""  FIFO caching """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching """
    def __init__(self):
        """ FIFO caching """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ FIFO caching """
        if key is None or item is None:
            return
        if len(self.keys) >= self.MAX_ITEMS:
            if key not in self.keys:
                print("DISCARD: {}".format(self.keys[0]))
                del self.cache_data[self.keys[0]]
            del self.keys[0]
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ FIFO caching """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
