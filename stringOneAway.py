# Implement your function below.
#O(n)
def is_one_away(s1, s2):
    if s1 == s2:
        return True
    ## find the index of differences O(n): dif_loc
    i = 0
    dif_loc = get_first_different_index(s1, s2)
    print("diff_loc {}".format(dif_loc))
    ## if same length: compare substring dif_loc-n O(n) 
    if (len(s1) == len(s2)):
        print("{} == {}: '{}' vs '{}'".format(s1, s2, s1[dif_loc+1:], s2[dif_loc+1:]))
        return get_first_different_index(s1[dif_loc+1:], s2[dif_loc+1:]) is None
    ## else: substrings: from dif_loc + 1 for the longer  and from dif_loc to n for the shorter O(n)
    elif len(s1) - 1== len(s2):
        print("{} > {}: '{}' vs '{}'".format(s1, s2, s1[dif_loc + 1:], s2[dif_loc:]))
        return get_first_different_index(s1[dif_loc + 1:], s2[dif_loc:]) is None
    elif len(s1)  == len(s2) - 1:
        print(" {} < {} '{}' vs '{}'".format(s1, s2, s1[dif_loc:], s2[dif_loc: + 1]))
        return get_first_different_index(s1[dif_loc:], s2[dif_loc + 1:]) is None
    else:
        return False

## O(max(n, m))
def get_first_different_index(s1, s2):
    if s1 == s2:
        return None;
    ## find the index of differences O(n): dif_loc
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] != s2[i]:
            return i;
        i += 1
    return i;

# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd"))  # should return True
print("--------------")
print(is_one_away("abde", "abcde")) # should return True
print("--------------")
print(is_one_away("a", "a"))  # should return True
print("--------------")
print(is_one_away("abcdef", "abqdef"))  # should return True
print("--------------")
print(is_one_away("abcdef", "abccef"))  # should return True
print("--------------")
print(is_one_away("abcdef", "abcde"))  # should return True
print("--------------")
print(is_one_away("aaa", "abc"))  # should return False
print("--------------")
print(is_one_away("abcde", "abc"))  # should return False
print("--------------")
print(is_one_away("abc", "abcde"))  # should return False
print("--------------")
print(is_one_away("abc", "bcc"))  # should return False

