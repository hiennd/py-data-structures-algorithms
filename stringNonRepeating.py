# Implement your function below.
import unittest
'''
O(n)
'''
def non_repeating(given_string):
    hist = dict()
    for c in given_string:
        hist[c] = hist.get(c, 0) + 1
    
    for k, v in hist.items():
        if v == 1:
            return k

    return None

# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'

class Tests(unittest.TestCase):
    def test_non_repeating(self):
        self.assertEqual(non_repeating("abcab"), 'c')
        self.assertEqual(non_repeating("aabbbc"), 'c')
        self.assertEqual(non_repeating("aabbdbc"), 'd')
    def test_only_repeating(self):
        self.assertEqual(non_repeating("abab"), None)
        
if __name__ == '__main__':
    unittest.main()