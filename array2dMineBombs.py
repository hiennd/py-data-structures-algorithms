# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for i, j in bombs:
        print("Bomb [{}, {}]".format(i, j))
        field[i][j] = -1
        for k in range(i -1, i + 2):
            for t in range(j - 1, j + 2):
                add_bomb_count(field, num_rows, num_cols, k, t)
    return field
    
def add_bomb_count(field, num_rows, num_cols, x, y):
    if x < 0 or x >= num_rows:
        return
    if y < 0 or y >= num_cols:
        return
    if field[x][y] == -1:
        return
    print("x={}, y={}".format(x, y))
    field[x][y] += 1
    print(to_string(field))
    


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
print( "mine_sweeper([[0, 2], [2, 0]], 3, 3)")
print( mine_sweeper([[0, 2], [2, 0]], 3, 3) )
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

# mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) should return:
print ("mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)")
print (mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) )
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) should return:
print("mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)")
print( mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) )
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]