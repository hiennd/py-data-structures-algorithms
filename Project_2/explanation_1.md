LRU_Cache
- Data Structure: OrderedDict / LinkedHashMap (Java)
 While it's clear to use a dictionary / HashMap for storing caches, because it has O(1) for accessing / checking containing operation, how to maintain the orders of those actions is quite challanged.
 A queue could be also usefull to check the order of recent used keys, but removing duplication keys could lead to worst case O(n).
 Ideally it is only required to maintain the orders of keys, so the easiest way is to choose an ordered dictionary / linked hash map to solve the problem, which has the runtime of O(1) for moving items to the end of the chain.
 - Runtime: O(1)
 operations on OrderedDict are constant as described above.
