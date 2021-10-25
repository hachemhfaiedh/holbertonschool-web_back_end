#!/usr/bin/env python3
""" Basic dictionary """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic dictionary """

    def put(self, key, item):
        """ Basic dictionary """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Basic dictionary """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
