import unittest
from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        '''
        Args:
        capacity: is Nullable for purpose of disabling caches
        '''
        # Initialize class variables
        pass
    
    def is_full(self):
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        pass
    
    '''
        Setting  into an empty LRU_Cache takes no effects but only warning
    '''
    def set(self, key, value):
        pass
        
class Test(unittest.TestCase):
    def test_given_queue_6_5_2_1_4__321_remove_key_3(self):
        print('------------------------------------------')
        print('test_given_queue_6_5_2_1_4_remove_key_3')
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(1, our_cache.get(1))      
        self.assertEqual(2, our_cache.get(2))     
        self.assertEqual(-1, our_cache.get(9))  
        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        self.assertEqual(-1, our_cache.get(3))     
            
        print(f'our_cache.get(3) = {our_cache.get(3)}')
        ## expected -1

    def test_given_queue_2_6_5_3_4__432_1_remove_key_1(self):
        print('------------------------------------------')
        print('test_given_queue_2_6_5_3_4remove_key_1')
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(4, our_cache.get(4))     
        self.assertEqual(3, our_cache.get(3))     
        self.assertEqual(-1, our_cache.get(9))  

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        self.assertEqual(2, our_cache.get(2))    
        self.assertEqual(-1, our_cache.get(1))   

        print(f'our_cache.get(1) = {our_cache.get(1)}')
        ## expected -1

    def test_given_queue_65_3443_1221_remove_key_2(self): 
        print('------------------------------------------')
        print('test_given_queue_2653_4_43_21_21_remove_key_2')
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1)
        our_cache.set(2, 2)
        self.assertEqual(2, our_cache.get(2))      
        self.assertEqual(1, our_cache.get(1))     
        our_cache.set(3, 3)
        our_cache.set(4, 4)

        self.assertEqual(4, our_cache.get(4))      
        self.assertEqual(3, our_cache.get(3))      
        self.assertEqual(-1, our_cache.get(9))    

        our_cache.set(5, 5) 
        our_cache.set(6, 6)

        self.assertEqual(-1, our_cache.get(2))  

        print(f'our_cache.get(2) = {our_cache.get(2)}')
        ## expected -1

    def test_given_queue_none_capacity_then_return_minus_one(self): 
        print('------------------------------------------')
        print('test_given_queue_2653_4_43_21_21_remove_key_2')
        our_cache = LRU_Cache(0)
        our_cache.set(2, 2)
        self.assertEqual(-1, our_cache.get(2))  
        print(f'our_cache.get(2) = {our_cache.get(2)}')
        ## expected -1
    

if __name__ == "__main__":
    unittest.main()