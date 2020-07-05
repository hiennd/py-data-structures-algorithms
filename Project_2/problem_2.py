import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = list()
    find_files_memoized(suffix, path, result)
    return result
    
def find_files_memoized(suffix, path, collector):

    ## Base Recursion O(1)
    if os.path.isfile(path):
        if not suffix or path.endswith(suffix):
            collector.append(path)
            return collector  ## return 'testdir/subdir1/a.h'
        return None
    elif not os.path.isdir(path):  
        return None       ##2. testdir/subdir1
    
    ## Recurrsive calls
    directories = os.listdir(path) ##['subdir4', 'subdir3', 't1.c', 'subdir2', 'subdir5', 't1.h', 'subdir1']  ##2. ## ['a.h', 'a.c']
    for directory in directories:
        find_files_memoized(suffix, path + '/' + directory, collector) ## testdir/subdir1  ##2.['testdir/subdir1/a.h', 'testdir/subdir1/a.c']
    return collector
##
def test_given_dirs_without_suffic():
    print('\n'.join(find_files(None, './Project_2/testdir')))
def test_given_dirs_with_suffic():
    print('\n'.join(find_files('.c', './Project_2/testdir')))
print('--------')
test_given_dirs_without_suffic()
print('--------')
test_given_dirs_with_suffic()