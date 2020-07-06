import unittest
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotation from a sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or None
    """
    if not input_list:
        return None
    pivot_index = binary_pivot_search(input_list) 
    if pivot_index == 0:
        return binary_search(input_list, number)
    if input_list[0] > number:
        ## go to smaller part
        if (input_list[0]  == 6 and  pivot_index == 0):
            print('debuging', input_list[pivot_index::])
        return binary_search(input_list[pivot_index::], number) + pivot_index
    else:
        ## go to the bigger part
        if (input_list[0]  == 6 and pivot_index == 0):
            print('debuging', input_list[0:pivot_index])
        return binary_search(input_list[0:pivot_index], number)


def binary_pivot_search(source, start_index = 0):
    end_index = len(source) - 1
    if start_index > end_index:
        return 0
    mid_index = (start_index + end_index) // 2

    if mid_index - 1 > 0 and source[mid_index] < source[mid_index - 1]:
        return mid_index

    if source[mid_index] > source[mid_index - 1]:
        return binary_pivot_search(source, start_index + 1)
    
def binary_search(source, target, start_index = 0, end_index = None):
    ## base condition O(1)
    if end_index is None:
        end_index = len(source) - 1

    if start_index > end_index:
         return None

    mid_index = (start_index + end_index) // 2

    if source[mid_index] == target:
        return mid_index

    ## recursive O(logn)
    if source[mid_index] < target:
        return binary_search(source, target, mid_index + 1, end_index)
    else:
        return binary_search(source, target, start_index, mid_index - 1)

def linear_search(input_list, number):
    if not input_list:
        return None
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return None


class TestSearch(unittest.TestCase):
    def test_find_pivot(self):
        self.assertEqual(5, binary_pivot_search([6, 7, 8, 9, 10, 1, 2, 3, 4]))
        self.assertEqual(3, binary_pivot_search([6, 7, 8, 1, 2, 3, 4]))
        self.assertEqual(0, binary_pivot_search([6, 7, 8, 9, 10, 11, 12]))
        self.assertEqual(6, binary_pivot_search([6, 7, 8, 9, 10, 11, 5]))

    def test_search(self):
        def test_function(message, test_case):
            input_list = test_case[0]
            number = test_case[1]
            found_index = rotated_array_search(input_list, number)
            print(f'Found {number} at index: {found_index}')
            self.assertEqual(linear_search(input_list, number), found_index)
            if linear_search(input_list, number) == found_index:
                print(f"{message}: Pass")
            else:
                print(f"{message}: Fail")

        test_function('First index', [[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
        test_function('Last index', [[6, 7, 8, 1, 2, 3, 4], 4])
        test_function('Second half index', [[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
        test_function('First half index', [[6, 7, 8, 1, 2, 3, 4], 8])
        test_function('Middle index', [[6, 7, 8, 1, 2, 3, 4], 1])
        test_function('Should not found', [[6, 7, 8, 1, 2, 3, 4], 10])
        test_function('empty array', [[], 10])
        test_function('Null array', [None, 10])
        test_function('Not rotated array', [[6, 7, 8, 9, 10], 6])


if __name__ == "__main__":
    unittest.main()