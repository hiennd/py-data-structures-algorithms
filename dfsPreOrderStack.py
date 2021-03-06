# Use this class to create binary trees.
import pdb
from collections import deque
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = { head_value: head }
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head

class State:
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
    def visit_left(self):
        self.visited_left = True
    def visit_right(self):
        self.visited_right = True

def print_pre_oreder(tree_node):
    visited_stack = []
    result = []
    current = tree_node
    state = State(current)
    visited_stack.append(state)
    result.append(current.value)
    while current:
        if current.left and not state.visited_left:
            state.visit_left()
            current = current.left
            result.append(current.value)
            state = State(current)
            visited_stack.append(state)
        elif current.right and not state.visited_right:
            state.visit_right()
            current = current.right
            result.append(current.value)
            state = State(current)   
            visited_stack.append(state)  
        else:
            visited_stack.pop()
            if len(visited_stack) != 0:
                state = visited_stack[-1]
                current = state.node
            else:
                state = None
                current = None
    return result


# NOTE: The following values will be used for testing your solution.

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping0 = {0: [1, 2]}
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
mapping4 = {3: [1, 5], 1: [0, 4]}
head0 = create_tree(mapping0, 0)
# This tree is:
#  head0 = 0
#        /   \
#       1     2
head1 = create_tree(mapping1, 0)
# This tree is:
#  head1 = 0
#        /   \
#       1     2
#      /\    / \
#     3  4  5   6
head2 = create_tree(mapping2, 3)
# This tree is:
#  head2 = 3
#        /   \
#       1     4
#      /\    / \
#     0  2  5   6
head3 = create_tree(mapping3, 3)
# This tree is:
#  head3 = 3
#        /   \
#       1     5
#      /\    / \
#     0  2  4   6
head4 = create_tree(mapping4, 3)
# This tree is:
#  head4 = 3
#        /   \
#       1     5
#      /\
#     0  4
print(print_pre_oreder(head0))
print(print_pre_oreder(head1))
print(print_pre_oreder(head2))
print(print_pre_oreder(head3))
print(print_pre_oreder(head4))