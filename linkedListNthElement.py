class Node:
    def __init__(self, value, child = None):
        self.value = value
        self.child = child

def nth_from_last(head, n):
    if head is None:
        return None
    left = head
    right = head

    ## move right n element farway
    for _ in range(n):
        if right is None:
            return None
        right = right.child

    ## move both to the end
    while right is not None:
        left = left.child
        right = right.child

    return left.value


def nth_from_last_by_size(head, n):
    if head is None:
        return None
    size = 1
    current = head
    # O(n)
    while current.child is not None:
        size += 1
        current = current.child
    if n > size:
        return None
    index = 0
    current = head
    # O(n)
    while index < size - n:
        current = current.child
        index += 1
    return current.value

# NOTE: Feel free to use the following function for testing.
# It converts the given linked list into an easy-to-read string format.
# Example: 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)
def linked_list_to_string(head):
    current = head
    str_list = []
    while current:
        str_list.append(str(current.value))
        current = current.child
    str_list.append('(None)')
    return ' -> '.join(str_list)


# NOTE: The following input values will be used for testing your solution.
current = Node(1)
for i in range(2, 8):
    current = Node(i, current)
head = current
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

current2 = Node(4)
for i in range(3, 0, -1):
    current2 = Node(i, current2)
head2 = current2
# head2 = 1 -> 2 -> 3 -> 4 -> (None)


# nth_from_last(head, 1) should return 1.
print(nth_from_last(head, 1))
# nth_from_last(head, 5) should return 5.
print(nth_from_last(head, 5)) 
# nth_from_last(head2, 2) should return 3.
print(nth_from_last(head2, 2))
# nth_from_last(head2, 4) should return 1.
print(nth_from_last(head2, 4))
# nth_from_last(head2, 5) should return None.
print(nth_from_last(head2, 5))
# nth_from_last(None, 1) should return None.
print(nth_from_last(None, 1))