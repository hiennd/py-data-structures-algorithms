import unittest
from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        '''
        Args:
        capacity: 0 for disabling caches
        '''
        # Initialize class variables
        self.bucket = OrderedDict()
        self.capacity = capacity
    
    def is_full(self):
        return len(self.bucket) >= self.capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if not self.capacity or key not in self.bucket:
            return -1
        value = self.bucket.get(key)
        self.bucket.move_to_end(key) 
        return value
    
    '''
        Setting  into an empty LRU_Cache takes no effects but only warning
    '''
    def set(self, key, value):
        if not self.capacity:
            print('Warn: Trying to set value into an empty caches.')
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.bucket and self.is_full():
            self.bucket.popitem(last = False) ## remove first in
        self.bucket[key] = value
        self.bucket.move_to_end(key)

class Test(unittest.TestCase):
    def test_given_queue_6_5_2_1_4__321_remove_key_3(self):
        print('------------------------------------------')
        print('test_given_queue_6_5_2_1_4_remove_key_3')
        test_caches = LRU_Cache(5)
        test_caches.set(1, 1)
        test_caches.set(2, 2)
        test_caches.set(3, 3)
        test_caches.set(4, 4)

        self.assertEqual(1, test_caches.get(1))      
        self.assertEqual(2, test_caches.get(2))     
        self.assertEqual(-1, test_caches.get(9))  
        test_caches.set(5, 5) 
        test_caches.set(6, 6)

        self.assertEqual(-1, test_caches.get(3))     
        print(f'test_caches.get(3) = {test_caches.get(3)}')

    def test_given_queue_2_6_5_3_4__432_1_remove_key_1(self):
        print('------------------------------------------')
        print('test_given_queue_2_6_5_3_4remove_key_1')
        test_caches = LRU_Cache(5)
        test_caches.set(1, 1)
        test_caches.set(2, 2)
        test_caches.set(3, 3)
        test_caches.set(4, 4)

        self.assertEqual(4, test_caches.get(4))     
        self.assertEqual(3, test_caches.get(3))     
        self.assertEqual(-1, test_caches.get(9))  

        test_caches.set(5, 5) 
        test_caches.set(6, 6)

        self.assertEqual(2, test_caches.get(2))    
        self.assertEqual(-1, test_caches.get(1))   
        print(f'test_caches.get(1) = {test_caches.get(1)}')

    def test_given_queue_65_3443_1221_remove_key_2(self): 
        print('------------------------------------------')
        print('test_given_queue_2653_4_43_21_21_remove_key_2')
        test_caches = LRU_Cache(5)
        test_caches.set(1, 1)
        test_caches.set(2, 2)
        self.assertEqual(2, test_caches.get(2))      
        self.assertEqual(1, test_caches.get(1))     
        test_caches.set(3, 3)
        test_caches.set(4, 4)

        self.assertEqual(4, test_caches.get(4))      
        self.assertEqual(3, test_caches.get(3))      
        self.assertEqual(-1, test_caches.get(9))    

        test_caches.set(5, 5) 
        test_caches.set(6, 6)

        self.assertEqual(-1, test_caches.get(2))  
        print(f'test_caches.get(2) = {test_caches.get(2)}')

    def test_given_queue_none_capacity_then_return_minus_one(self): 
        print('------------------------------------------')
        print('test_given_queue_2653_4_43_21_21_remove_key_2')
        test_caches = LRU_Cache(0)
        test_caches.set(2, 2)
        self.assertEqual(-1, test_caches.get(2))  
        print(f'test_caches.get(2) = {test_caches.get(2)}')    

if __name__ == "__main__":
    unittest.main()
