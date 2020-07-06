import unittest
import timeit
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return is_user_in_group_mem(user, group, dict())

def is_user_in_group_mem(user, group, marker):
    ## Base Condition: O(n) where n is max-number of users in one group
    if group in marker:
        return marker[group]
    resutl = False
    if user in group.users:
        marker[group] = True
        resutl = True
    else:
        marker[group] = False
    ## Recurrsive calls
    for sub_group in group.get_groups():
        return is_user_in_group_mem(user, sub_group, marker)
    return resutl

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)
## sub_child_belongs_to_many_groups
'''
Please node that this will increase total runtime of the py script itself but not the solution
'''
for i in range(1_000_000):
    parent.add_group(   Group('Child2' + str(i)).add_group(sub_child) )

class TestClass(unittest.TestCase):


    def test_looking_up_within_users(self):
        self.assertTrue(is_user_in_group(sub_child_user, sub_child))
    def test_looking_up_groups_in_group(self):
        self.assertTrue(is_user_in_group(sub_child_user, child))
    def test_looking_up_three_levels(self):
        self.assertTrue(is_user_in_group(sub_child_user, parent))
    
    def test_duplicates_sub_child_in_groups(self):
        start = timeit.default_timer()
        self.assertTrue(is_user_in_group(sub_child_user, parent))
        stop =  timeit.default_timer()
        print(f'test_1000_duplicates_sub_child_in_groups: {stop - start}')
    
if __name__ == '__main__':
    unittest.main()