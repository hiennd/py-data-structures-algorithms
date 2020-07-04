# Use this class to create binary trees.
import unittest
from collections import deque
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    # Overriding the equality operator.
    # This will be used for testing your solution.
    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False


# Implement your function below.
def lca(root, j, k):
    if root is None:
        return None
    ## find path to 8 is (5, 1, 8)
    j_path = find_path(root, j)

    if j_path is None:
        return None
    print(f'j_path:', *j_path)
    ## find path to 7 is (5, 1,3)
    k_path = find_path(root, k)
    if k_path is None:
        return None
    print(f'k_path:', *k_path)
    ## find less comon ancestor is 1
    lce_common = None
    print(f'len(j_path)={len(j_path)}')
    while len(j_path) != 0 and len(k_path) != 0:
        j_pop = j_path.pop()
        k_pop = k_path.pop()
        if j_pop == k_pop:
            lce_common = j_pop
        else:
            break
    return lce_common
def find_path(node, i):
    print(f'Calling find_path({node}, {i})')
    if node.value == i:
        return deque([node])
    if node is None:
        return None
    if node.left:
        left_path = find_path(node.left, i) ## node_1, 8 -> node_3, 8 -> node_6, 8 --> return null
        if left_path:
            left_path.append(node)
            print(f'returning left_path', *left_path)
            return left_path
    if node.right:  ## 1st at node_3
        right_path = find_path(node.right, i) ## call node_7, 7 ---> return Stack[node_7]
        if right_path: 
            print(f'returning right_path', *right_path)
            right_path.append(node)
            return right_path
    return None
    


# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


# NOTE: The following values will be used for testing your solution.

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
head1 = create_tree(mapping1, 0)
# This tree is:
# head1 = 0
#        / \
#       1   2
#      /\   /\
#     3  4 5  6


mapping2 = {5: [1, 4], 1: [3, 8], 4: [9, 2], 3: [6, 7]}
head2 = create_tree(mapping2, 5)
# This tree is:
#  head2 = 5
#        /   \
#       1     4
#      /\    / \
#     3  8  9  2
#    /\
#   6  7


#lca(head1, 1, 5) should return 0
#print( lca(head1, 1, 5) )
# lca(head1, 3, 1) should return 1
# print( lca(head1, 3, 1) )
# lca(head1, 1, 4) should return 1
# print (lca(head1, 1, 4) )
# lca(head1, 0, 5) should return 0
# lca(head2, 4, 7) should return 5
# lca(head2, 3, 3) should return 3
# lca(head2, 8, 7) should return 1
print( lca(head2, 8, 7) )
# lca(head2, 3, 0) should return None (0 does not exist in the tree)

class TestLCA(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, lca(head1, 1, 5).value)
    def test_2(self):
        self.assertEqual(1, lca(head1, 3, 1).value)
    def test_3(self):
        self.assertEqual(1, lca(head1, 1, 4).value)
    def test_4(self):
        self.assertEqual(0, lca(head1, 0, 5).value)
    def test_5(self):
        self.assertEqual(5, lca(head2, 4, 7).value)    
    def test_6(self):
        self.assertEqual(3, lca(head2, 3, 3).value)
    def test_7(self):
        self.assertEqual(1, lca(head2, 8, 7).value)
    def test_None(self):
        self.assertEqual(None, lca(head2, 3, 0))

if __name__ == "__main__":
    unittest.main()

