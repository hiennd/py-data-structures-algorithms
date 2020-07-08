
import unittest
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       [(int),(int)]: of two maximum sums if there are more than two elements in the list, else None.
    """
    if not input_list or len(input_list) < 2:
        return None
    ## step 1 sort with merge-sort O(nlogn) [2, 4, 5, 6, 8, 9]
    sorted_list = merge_sort(input_list)
    ## step 2 build first number from odds postions 964 and even postions 852
    number_1_str = ''
    number_2_str = ''
    for i in range(1, len(sorted_list) + 1):
        if i % 2 != 0:
            number_1_str += str(sorted_list[-i])
        else:
            number_2_str += str(sorted_list[-i])
    number_1 = int(number_1_str)
    number_2 = int(number_2_str)
    if number_1 > number_2:
        return [number_1, number_2]
    else:
        return [number_2, number_1]

def merge_sort(input_list):
    ## base
    if (len(input_list) == 1):
        return input_list
    ## devide
    mid_index = len(input_list) // 2
    left_list = input_list[:mid_index]
    right_list = input_list[mid_index:]
    ## sort
    sorted_left = merge_sort(left_list)
    sorted_right = merge_sort(right_list)
    ## merge two halves
    return merge(sorted_left, sorted_right)
    
##  self.assertEquals([0,1, 2, 3, 6, 9], merge([0 , 2, 3], [1, 6 , 9]))
def merge(list_1, list_2):
    i = 0
    j = 0
    merged = []
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            merged.append(list_1[i])
            i += 1
        else:
            merged.append(list_2[j])
            j += 1
    merged += list_1[i:]  
    merged += list_2[j:]
    return merged

class TestRearrangeDigits(unittest.TestCase):

    def test_rearrange_digits(self):
        print(f'Test rearrange_digits([1, 2, 3, 4, 5]) expected [542, 31]. Found:{rearrange_digits([1, 2, 3, 4, 5])}')
        self.assertEqual([531, 42], rearrange_digits([1, 2, 3, 4, 5]))

        print(f'rearrange_digits([4, 6, 2, 5, 9, 8]) expected [964, 852]. Found {rearrange_digits([4, 6, 2, 5, 9, 8])}')
        self.assertEqual([964, 852], rearrange_digits([4, 6, 2, 5, 9, 8]))
    
    def test_rearrange_digits_empty(self):
        self.assertEqual(None, rearrange_digits([]))
    
    def test_rearrange_digits_one_digit(self):
        self.assertEqual(None, rearrange_digits(['1']))

    def test_rearrange_digits_two_digits(self):
        self.assertEqual([2, 1], rearrange_digits(['1', '2']))

    def test_rearrange_digits_None(self):
        self.assertEqual(None, rearrange_digits(None))

    def test_merge_two_sorted_lists(self):
        self.assertEqual([0,1, 2, 3, 6, 9], merge([0, 2, 3], [1, 6, 9]))
        self.assertEqual([0,2,3], merge([0, 2, 3], []))
        self.assertEqual([], merge([], []))
        
    def test_merge_sorting(self):
        self.assertEqual([1, 2, 3, 4, 5], merge_sort([1, 2, 3, 4, 5]))
        self.assertEqual( [2, 4, 5, 6, 8, 9], merge_sort( [4, 6, 2, 5, 9, 8] ))
if __name__ == "__main__":
    unittest.main()