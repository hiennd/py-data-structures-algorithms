**LRU_Cache**
**Data Structure:**
- Data Structure: OrderedDict (python) / LinkedHashMap (Java)
 While it's clear to use a dictionary / HashMap for storing caches, because it has O(1) for accessing / checking containing operation, how to maintain the orders of those actions is quite challengued.
 A queue could be also usefull to check the order of recent used keys, but removing duplication keys could lead to worst case O(n).
 Ideally it is only required to maintain the orders of keys, so the easiest way is to choose an ordered dictionary / linked hash map to solve the problem, which has the runtime of O(1) for moving items to the end of the chain, and space of O(n) with implementation from python3.
**Time Complexity Analysis**
 - Runtime: O(1)
 The operations on OrderedDict which are used in the solution are constant.
 **Space Complexity Analysis**
 - Space: O(n)
 as a result of using (doubly) linked list
