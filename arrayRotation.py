import unittest
# Implement your function below.
'''
O(n)
'''
def is_rotation(list1, list2):
    ## check length
    n = len(list1)
    if len(list1) != len(list2):
        return False

    first_element_index = -1
    for i in range(n):
        if list1[0] == list2[i]:
            first_element_index = i
            break
    print("first_element_index {}".format(first_element_index))
    if first_element_index == -1:
        return False
    
    ## check first part
    for i in range(n):
        j =  ( first_element_index + i ) % n
        print("list1[{}] {} == list2[{}] {}".format(i, list1[i], j, list2[j]))
        if list1[i] != list2[j]:
            return False
    return True

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.

class Test_Array_Rotaion(unittest.TestCase):

    def test_rotate_a(self):
        self.assertFalse(is_rotation(list1, list2a))
    def test_rotate_b(self):
        self.assertTrue(is_rotation(list1, list2b))
    def test_rotate_c(self):
        self.assertFalse(is_rotation(list1, list2c))
    def test_rotate_d(self):
        self.assertFalse(is_rotation(list1, list2d))
    def test_rotate_e(self):
        self.assertFalse(is_rotation(list1, list2e))
    def test_rotate_f(self):
        self.assertTrue(is_rotation(list1, list2f))
    def test_rotate_g(self):
        self.assertTrue(is_rotation(list1, list2g))

if __name__ == '__main__':
    unittest.main()