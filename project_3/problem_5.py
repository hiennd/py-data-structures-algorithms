from collections import defaultdict
from collections import deque
import unittest

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = defaultdict()
    
    def insert(self, char):
        """Add a child node in this Trie
        
        Returns: A TrieNode after inserting
        
        Args: 
            char: charater to add
        """
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        def suffixes_recursive(node, suffix = '', collector = []):
            ## base
            if node.is_word:
                collector.append(''.join(suffix))
            if len(node.children) == 0:
                return collector
            ## recursive
            for char in node.children:
                child_suffix = suffix + char
                suffixes_recursive(node.children[char], child_suffix, collector)
        collector = []
        suffixes_recursive(self, '', collector)
        return collector
    
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            current_node = current_node.insert(char)
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if not prefix:
            return None
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        return current_node

class TestClass(unittest.TestCase):
    def test_trie(self):
        # Add words
        valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
        word_trie = Trie()
        for valid_word in valid_words:
            word_trie.insert(valid_word)

        # Tests
        self.assertTrue(word_trie.find('the'))
        self.assertTrue(word_trie.find('any'))
        self.assertFalse(word_trie.find('these'))
        self.assertFalse(word_trie.find('zzzz'))

    def test_suffixes_two_chars_on_large_words_list(self):
        valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
        word_trie = Trie()
        for valid_word in valid_words:
            word_trie.insert(valid_word)
        
        prefix_node = word_trie.find('th')
        print("test_suffixes_two_chars th")
        self.assertEqual(['e', 'ere', 'eir'], prefix_node.suffixes())

    def test_suffixes_one_char_on_large_words_list(self):
        test_trie = Trie()
        word_list = [
                    "ant", "anthology", "antagonist", "antonym", 
                    "fun", "function", "factory", 
                    "trie", "trigger", "trigonometry", "tripod"]
        for word in word_list:
            test_trie.insert(word)        
        
        prefix_node = test_trie.find('f')
        print("test_suffixes_one_char f")
        self.assertEqual(['un', 'unction', 'actory'], prefix_node.suffixes())

    def test_suffixes_three_chars(self):
        test_trie = Trie()
        word_list = [
                    "ant", "anthology", "antagonist", "antonym", 
                    "fun", "function", "factory", 
                    "trie", "trigger", "trigonometry", "tripod"]
        for word in word_list:
            test_trie.insert(word)        
        
        prefix_node = test_trie.find('tri')
        print("test_suffixes_three_chars tri")
        self.assertEqual(['e', 'gger', 'gonometry', 'pod'], prefix_node.suffixes())
    
    def test_suffixes_three_chars_on_small_words_list(self):
        test_trie = Trie()
        word_list = ["trio"]
        for word in word_list:
            test_trie.insert(word)        
        
        prefix_node = test_trie.find('tri')
        print("test_suffixes_three_chars_on_small_words_list tri")
        self.assertEqual(['o'], prefix_node.suffixes())

    def test_suffixes_empty(self):
        test_trie = Trie()
        word_list = [
                    "ant", "anthology", "antagonist", "antonym", 
                    "fun", "function", "factory", 
                    "trie", "trigger", "trigonometry", "tripod"]
        for word in word_list:
            test_trie.insert(word)        
        
        print("test_suffixes_empty ' '")
        prefix_node = test_trie.find('')
        self.assertEqual(None, prefix_node)

    def test_suffixes_none(self):
        test_trie = Trie()
        word_list = [
                    "ant", "anthology", "antagonist", "antonym", 
                    "fun", "function", "factory", 
                    "trie", "trigger", "trigonometry", "tripod"]
        for word in word_list:
            test_trie.insert(word)        
        
        print("test_suffixes_none none")
        prefix_node = test_trie.find(None)
        self.assertEqual(None, prefix_node)
        
if __name__ == "__main__":
    unittest.main()

