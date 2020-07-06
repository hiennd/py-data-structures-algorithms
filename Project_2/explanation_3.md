**Huffman coding**
**Data Structure:**
- Data Structure: Priority Queue implemented by Heap
Everytime two node are merged into one new node, the queue needed to be sorted for reinsertion. Using Priority can offer best time running.
I use the python heapy for some basics operations: push and pop with O(logN) and O(1) corresponding run-time.
Using this module, the class HuffmanNode has to maintain a tree structure, which is slightly more spaces required to save left and right chilren.
Because building HuffmanTree is kind of map and reduce, so it's fine, there is no duplication in memory for saving all nodes in the tree structures.
Besides, using tree structure increas code readability, compared to jumping indecies in an array.
**Time Complexity Analysis**
 - Runtime: O(nlogn), n is the length of input string /text
We need to go through all characters so it requires at least O(n) then we need to heapify from them, it takes O(nlogn)
Sorting and Resorting take only O(logn) with the benefit of Priority Queue with Heap.
 **Space Complexity Analysis**
 - Space: O(n)
in the worst case if text has no duplication, i.e. all frequencies = 1.