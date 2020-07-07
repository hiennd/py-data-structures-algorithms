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
            return collector  
        return None
    elif not os.path.isdir(path):  
        return None      
    
    ## Recurrsive calls
    directories = os.listdir(path) 
    for directory in directories:
        find_files_memoized(suffix, path + '/' + directory, collector)
    return collector
##
def test_given_dirs_without_suffic():
    print('\n'.join(find_files(None, './Project_2/testdir')))
def test_given_dirs_with_suffic_c():
    print('\n'.join(find_files('.c', './Project_2/testdir')))
def test_given_dirs_with_suffic_h():
    print('\n'.join(find_files('.h', './Project_2/testdir')))
def test_given_dirs_with_empty_suffic():
    print('\n'.join(find_files('', './Project_2/testdir')))
def test_given_dirs_with_not_found_suffic():
    print('\n'.join(find_files('boeser', './Project_2/testdir')))
print('--------')
test_given_dirs_without_suffic()
## expected: 
# ./Project_2/testdir/subdir4/.gitkeep
# ./Project_2/testdir/subdir3/subsubdir1/b.h
# ./Project_2/testdir/subdir3/subsubdir1/b.c
# ./Project_2/testdir/t1.c
# ./Project_2/testdir/subdir2/.gitkeep
# ./Project_2/testdir/subdir5/a.h
# ./Project_2/testdir/subdir5/a.c
# ./Project_2/testdir/t1.h
# ./Project_2/testdir/subdir1/a.h
# ./Project_2/testdir/subdir1/a.c
print('--------')
test_given_dirs_with_suffic_c()
## expected:
# ./Project_2/testdir/subdir3/subsubdir1/b.c
# ./Project_2/testdir/t1.c
# ./Project_2/testdir/subdir5/a.c
# ./Project_2/testdir/subdir1/a.c
print('--------')
test_given_dirs_with_suffic_h()
## expected
# ./Project_2/testdir/subdir3/subsubdir1/b.h
# ./Project_2/testdir/subdir5/a.h
# ./Project_2/testdir/t1.h
# ./Project_2/testdir/subdir1/a.h
print('--------')
test_given_dirs_with_empty_suffic()
## expected: 
# ./Project_2/testdir/subdir4/.gitkeep
# ./Project_2/testdir/subdir3/subsubdir1/b.h
# ./Project_2/testdir/subdir3/subsubdir1/b.c
# ./Project_2/testdir/t1.c
# ./Project_2/testdir/subdir2/.gitkeep
# ./Project_2/testdir/subdir5/a.h
# ./Project_2/testdir/subdir5/a.c
# ./Project_2/testdir/t1.h
# ./Project_2/testdir/subdir1/a.h
# ./Project_2/testdir/subdir1/a.c
print('--------')
test_given_dirs_with_not_found_suffic()
## expected: empty