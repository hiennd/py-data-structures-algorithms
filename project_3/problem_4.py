import unittest
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        return None
    if len(input_list) == 0:
        return []
    ## First define three pointers to partion the list into 4 sections: 0s, 1s, sorting, 2s
    low_index = 0
    mid_index = 0
    high_index = len(input_list) - 1
    ## Now traverse the list with 3 pointers
    while mid_index <= high_index:
        if input_list[mid_index] == 0:
            swap(input_list, low_index, mid_index)
            low_index += 1
            mid_index += 1
        elif input_list[mid_index] == 1:
            mid_index += 1
        else:
            swap(input_list, mid_index, high_index)
            high_index -= 1
    return input_list

def swap(input_list, i, j):
    input_list[i], input_list[j] = input_list[j], input_list[i]

class TestSort012(unittest.TestCase):
    def test_sort_012(self):
        def test_with_sorted_result(test_case):
            print(f'expected {sorted(test_case)} from test case {test_case}. ')
            sorted_array = sort_012(test_case)
            print(f'result   {sorted_array}')
            if sorted_array == sorted(test_case):
                print("Pass")
                return 'Pass'
            else:
                print("Fail")
                return None

        self.assertEqual('Pass', test_with_sorted_result([0, 0, 1, 2, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
        self.assertEqual('Pass', test_with_sorted_result([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
        self.assertEqual('Pass', test_with_sorted_result([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
        self.assertEqual('Pass', test_with_sorted_result([0, 0, 0, 0, 0, 0]))
        self.assertEqual('Pass', test_with_sorted_result([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]))
        self.assertEqual('Pass', test_with_sorted_result([2, 2, 2, 2, 2, 2, 0, 0, 0, 0]))
        self.assertEqual([], sort_012([]))
        self.assertEqual(None, sort_012(None))

if __name__ == "__main__":
    unittest.main()