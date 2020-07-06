**Union and Intersection of Two Linked Lists**
**Datas tructure**
- LinkedList
- HashSet
**Time Complexity Analysis**
By building up a hash set to look up the common / non-common element, we have to traverse two list one by one so:
 1. Union: O(max(m,n)) where m, n are the length of two lists
 2. Intersection: O(max(m,n)) where m, n are the length of two lists
 **Space Complexity Analysis**
 - Space: O(n)
 1. Union: at most O(m + n) because of the space for the extra hashset of at most m +n elements from two lists.
 2. Intersection: at most O(2(m + n)) because of the space for two hashsets of at most m +n elements from two lists.
