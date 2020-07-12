**Autocomplete with Tries**
**Time Complexity**
Let's calculate the Time Complexity of `find(self, prefix)`. It is O(n) where n is the length of prefix as result of the loop.  Accessing to the dict() has auxilary complexity of O(1)
How about the Time Complexity of `suffixes(self, suffix = '')`. It is O(n * m) where n is number of nodes and m is the longest lenth words
There fore Time Complexity of Autocomplete is O(n * m)
**Spcace Complexity**
- Space of Trie tree: O(n *m) n is number of nodes and m is the average lenth words
- In the function 'suffixes_recursive(node, suffix = '', collector = [])', suffix and collector are reused so no extra spaces required.