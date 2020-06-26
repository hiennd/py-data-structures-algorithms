import copy
import math


# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    for i in range(math.floor(n/2)):
        for j in range(math.ceil(n/2)):
            tmp = []
            ( current_i, current_j ) = ( i, j )
            ## save four items in a rotation
            for k in range(4):
                tmp.append(given_array[current_i][current_j])
                # print(tmp)
                ( current_i, current_j )= new_loc(current_i, current_j, n)
            ## rotate them
            for k in range(4):
                given_array[current_i][current_j] = tmp[(k -1) % 4]
                ( current_i, current_j ) = new_loc(current_i, current_j, n)
            
    return given_array

def rotate_2(given_array, n):
    rotated = [[0 for j in range(n)] for i in range(n)]
    print(rotated)
    for i in range(n):
        for j in range(n):
            rotated[new_i][new_j] = given_array[i][j]
            new_i, new_j = new_loc(i, j, n)
    return rotated

def new_loc(i, j, n):
    return (j, n - 1 - i)

def rotate_1(given_array, n):
    rotated = [[] for i in range(n)]
    print(rotated)
    # NOTE: To solve it in place, write this function so that you
    for u_index in range(n):
        for i in range(n):
            rotated[i].insert(0, given_array[u_index][i])
    # won't have to create rotated.
    return rotated


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# rotate(a1, 3) should return:
print(to_string(rotate(a1, 3)))
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
# rotate(a2, 4) should return:
print(to_string(rotate(a2, 4)))
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]
