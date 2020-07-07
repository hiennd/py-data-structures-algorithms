class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values = None):
        self.head = None
        if values:
            for value in values:
                self.append(value)

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union_dict = dict()
    node = llist_1.head
    while node:
        union_dict[node.value] = '-'
        node = node.next
    
    node = llist_2.head
    while node:
        if not node.value in union_dict:
            union_dict[node.value] = '-'
        node = node.next
    return LinkedList(union_dict.keys())

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_dict = dict()
    node = llist_1.head
    while node:
        intersection_dict[node.value] = '-'
        node = node.next
    node = llist_2.head
    while node:
        if node.value in intersection_dict:
            intersection_dict[node.value] = 'common'
        node = node.next
    result = { key:value for (key,value) in intersection_dict.items() if value == 'common'}
    return LinkedList(result.keys())


# Test case 1
print('____Test___Case___1')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print ('        ', union(linked_list_1,linked_list_2))
print('expected 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> ')

print ('        ', intersection(linked_list_1,linked_list_2))
print('expected 4 -> 6 -> 21 -> ')

# Test case 2
print('____Test___Case___2')
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ('         ', union(linked_list_3,linked_list_4))
print('expected: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> ')
## expected empty []
print (intersection(linked_list_3,linked_list_4))
print('expected empty')

# Test case 3
print('____Test___Case___3')
linked_list_5 = LinkedList([1, 2, 3])
linked_list_6 = LinkedList([])
## expected 1 - 2 - 3
print ('         ', union(linked_list_5,linked_list_6))
print('expected  1 -> 2 -> 3 -> ')
## expected empty
print (intersection(linked_list_5,linked_list_6))
print('expected empty')


# Test case 3
print('____Test___Case___3')
linked_list_7 = LinkedList([])
linked_list_8 = LinkedList([])
## expected 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print ('         ', union(linked_list_7,linked_list_8))
print('expected  empty')
## expected empty
print (intersection(linked_list_7,linked_list_8))
print('expected empty')