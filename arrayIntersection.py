# Implement your function below.
'''
O(max(n, m)
'''
def common_elements(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        print("i={} j={} a={} b={}".format(i, j, a[i], b[j]))
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else: ## ai < bj
            i +=1
    return result


# NOTE: The following input values will be used for testing your solution.
list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).

