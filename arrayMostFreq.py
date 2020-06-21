# Implement your function below.
import unittest

'''
O(n)
'''
def most_frequent(arr):
    if (len(arr) == 0):
        return None
    elif len(arr) == 1:
        return arr.pop()
    max = 0
    result = None
    hist = dict()
    for num in arr:
        hist[num] = hist.get(num, 0) + 1
    for num, fq in hist.items():
        if max < fq:
            max = fq
            result = num
    return result

# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

class TestMe(unittest.TestCase):
    def test_1(self):
        self.assertEqual(most_frequent(list1), 1)
    def test_2(self):
        self.assertEqual(most_frequent(list2), 3)
    def test_3(self):
        self.assertEqual(most_frequent(list3), None)
    def test_4(self):
        self.assertEqual(most_frequent(list4), 0)
    def test_5(self):
        self.assertEqual(most_frequent(list5), -1)

if __name__ == "__main__":
    unittest.main()