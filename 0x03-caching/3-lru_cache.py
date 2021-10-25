#!/usr/bin/env python3
""" LRU Caching """


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching """
    def __init__(self):
        """ LRU Caching """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ LRU Caching """
        if key is None or item is None:
            return
        if len(self.keys) >= self.MAX_ITEMS:
            if key not in self.keys:
                print("DISCARD: {}".format(self.keys[-1]))
                del self.cache_data[self.keys[-1]]
            del self.keys[-1]
        self.keys = [key] + self.keys
        self.cache_data[key] = item

    def get(self, key):
        """ LRU Caching """
        if not key or key not in self.cache_data.keys():
            return None
        del self.keys[self.keys.index(key)]
        self.keys = [key] + self.keys
        return self.cache_data[key]
