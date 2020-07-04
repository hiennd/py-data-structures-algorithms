import unittest
import timeit
from collections import deque
class Queue():
    def __init__(self):
        self.items = deque()
    def enque(self, data):
        self.items.appendleft(data)
    def deque(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
        
    def __str__(self):
        return ' '.join([str(item) for item in self.items])


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.bucket = dict()
        self.queue = Queue()
        self.capacity = capacity
    
    def is_full(self):
        return len(self.bucket) >= self.capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.bucket:
            return -1
        value = self.bucket.get(key)
        if self.queue.size() == self.capacity - 1:
            self.queue.deque()
        self.queue.enque(key)
        print(f'Queue', self.queue)
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.bucket and self.is_full():
            to_remove_key = self.queue.deque()
            if to_remove_key == key:
                to_remove_key = self.queue.deque()
            print(f'To remove {to_remove_key}')
            self.bucket.pop(to_remove_key)
        self.bucket[key] = value
        self.queue.enque(key)
        if self.queue.size() == self.capacity - 1:
            self.queue.deque()
        print(f'Queue', self.queue)

class Test(unittest.TestCase):
    def test(self):
        start_time = timeit.default_timer()
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

        stop_time = timeit.default_timer()

        print(f'Runtime = {stop_time - start_time}')

if __name__ == "__main__":
    unittest.main()