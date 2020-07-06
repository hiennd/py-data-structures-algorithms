**Active Directory**

**Data Structure:**
- Data Structure: Lists in Lists, recursion, hash table.
1. The relationships is users - groups (many to many) and as well groups - groups (many to many).
There are also nested items.
So it seems like using hashmap / hashtable would increase complexity of the problem itself.
2. Using recursion for traversing nested lists with help from a dictionary.

**Time Complexity Analysis**
 - Runtime: worst O(n^m) but auxilary O(n), where n is number of directories and m is max number of customers within any directory.
For the recursion:
- There is at most (n + 1) calls of `is_user_in_group_mem(user, group, marker)`, with n is total directories.
- Each of those call has a base condtion  in the worst case of O(m) where m is the max users in a group. But it is actually O(1) if the directory is traversed at any intersteps.
 **Space Complexity Analysis**
 - Space: O(max(n,m))
where n is number of directories and m is max number of customers within any directory.