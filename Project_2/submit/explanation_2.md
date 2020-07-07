
**find_files(suffix, path()**

**Space Complexity Analysis**
- Space: O(n)
Each recursive call to the `find_files(suffix, path()` reuse variables: suffix, path and a collector list.
so space complexity only O(n), where n is the total number of (flatten) directories and files.

**Time Complexity Analysis**
- Time: O(n)
The base recurrsion has O(1)
The function `find_files_memoized(suffix, path, collector)`is called n times + 1, where n is the total number of (flatten) directories and files.
So the runtime is at most 2n + 1, which is O(n).
