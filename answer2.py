import datetime
import math


class Cache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.hash_table = dict()

    def is_cache_full(self):
        return len(self.hash_table) == self.cache_size

    def put(self, key, value, weight):
        if key not in self.hash_table:
            if self.is_cache_full():
                now = datetime.datetime.now()
                pop_key = None
                for key2, value2 in self.hash_table.items():
                    score = value2[1] / math.log(float((now-value2[2]).total_seconds()))
                    if not pop_key:
                        pop_key = [key2, score]
                    else:
                        if score < pop_key[1]:
                            pop_key = [key2, score]
                self.hash_table.pop(pop_key[0])
            last_access_time = datetime.datetime.now()
            self.hash_table[key] = [value, weight, last_access_time]

    def get(self, key):
        if key not in self.hash_table:
            return -1
        else:
            self.hash_table[key][2] = datetime.datetime.now()
            return self.hash_table[key][0]

# computational complexity of get(key) is O(1)
# computational complexity of put(...) is O(n)
