import unittest
from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.bucket = OrderedDict()
        self.capacity = capacity
    
    def is_full(self):
        return len(self.bucket) >= self.capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.bucket:
            print(f'Bucket afer getting {key}:', str(self.bucket))
            return -1
        value = self.bucket.get(key)
        self.bucket.move_to_end(key) 
        print(f'Bucket afer getting {key}:', str(self.bucket))
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.bucket and self.is_full():
            self.bucket.popitem(last = False) ## remove first in
        self.bucket[key] = value
        self.bucket.move_to_end(key)
        print(f'Bucket afer setting {key}:', str(self.bucket))

        
class Test(unittest.TestCase):
    def test_given_queue_6_5_2_1_4__321_then_remove_key_3(self):
        print('test_given_queue_6_5_2_1_4_remove_key_3')
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(1, our_cache.get(1))      # returns 1
        self.assertEqual(2, our_cache.get(2))      # returns 2
        self.assertEqual(-1, our_cache.get(9))    # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        self.assertEqual(-1, our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    def test_given_queue_2_6_5_3_4__432_1_then_remove_key_1(self):
        print('test_given_queue_2_6_5_3_4remove_key_1')
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(4, our_cache.get(4))      # returns 4
        self.assertEqual(3, our_cache.get(3))      # returns 3
        self.assertEqual(-1, our_cache.get(9))    # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        self.assertEqual(2, our_cache.get(2))    
        self.assertEqual(-1, our_cache.get(1))   # returns -1 because the cache reached it's capacity and 1 was the least recently used entry

    def test_given_queue_65_3443_1221_then_remove_key_2(self): 
        print('test_given_queue_2653_4_43_21_21_remove_key_2')
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        self.assertEqual(2, our_cache.get(2))      # returns 2
        self.assertEqual(1, our_cache.get(1))      # returns 1
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(4, our_cache.get(4))      # returns 4
        self.assertEqual(3, our_cache.get(3))      # returns 3
        self.assertEqual(-1, our_cache.get(9))    # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        self.assertEqual(-1, our_cache.get(2))   # returns -1 because the cache reached it's capacity and 2 was the least recently used entry
    

if __name__ == "__main__":
    unittest.main()