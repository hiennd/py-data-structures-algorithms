# Implement your function below.
# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'

def click(field, num_rows, num_cols, given_i, given_j):
    if field[given_i][given_j] != 0:
        return field
    to_check = set()
    to_check.add((given_i, given_j))
    while len(to_check) != 0:
        i, j = to_check.pop()
        for r in range(i - 1, i + 2):
            for c in range(j - 1, j + 2):
                if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
                    continue
                if field[r][c] == 0:
                    field[r][c] = -2
                    to_check.add((r, c))
    return field
    
# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 2, 2) should return:
print("click(field1, 3, 5, 2, 2)")
print(to_string( click(field1, 3, 5, 2, 2) ))
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 1, 4) should return:
print("click(field1, 3, 5, 1, 4)")
print(to_string( click(field1, 3, 5, 1, 4) ))
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# click(field2, 4, 4, 0, 1) should return:
print("to_string( click(field2, 4, 4, 0, 1) )")
print(to_string( click(field2, 4, 4, 0, 1) ))
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

# click(field2, 4, 4, 1, 3) should return:
print("to_string( click(field2, 4, 4, 1, 3) )")
print(to_string( click(field2, 4, 4, 1, 3) ))
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
