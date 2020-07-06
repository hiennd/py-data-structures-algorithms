import sys
import heapq
import unittest
class HuffermanNode(object):
    def __init__(self, freq, char = None, left =  None, right = None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    ## getter and setter omitted
    def merge(self, node2):
        if self < node2:
            return HuffermanNode(self.freq + node2.freq, None, self, node2)
        return HuffermanNode(self.freq, None, node2, self)
    def __lt__(self, value):
        return self.freq < value.freq
    def get_codes(self):
        codes = dict()
        def code_char(s, hf_node):
            if hf_node is None:
                return
            if hf_node.char:
                if not s:
                    codes[hf_node.char] = '0'
                else:
                    codes[hf_node.char] = s
            else:
                code_char(s + '0', hf_node.left)
                code_char(s + '1', hf_node.right)
        code_char('', self)
        return codes

def huffman_encoding(data):
    ## build historgram O(n)
    hist = dict()
    for char in data:
        hist[char] = hist.get(char, 0) + 1
    ## build tree. Time: O(logn) Space: O(n)
    hf_heap = [HuffermanNode(v, k) for k, v in hist.items()]
    heapq.heapify(hf_heap)
    while len(hf_heap) > 1:
        min_element_1 = heapq.heappop(hf_heap)
        min_element_2 = heapq.heappop(hf_heap)
        merged_elment = min_element_1.merge(min_element_2)
        heapq.heappush(hf_heap, merged_elment)
    hf_tree = hf_heap[0]
    codes = hf_tree.get_codes()
    ### encoding. Time: O(n)
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]
    return (encoded_data, hf_tree)

## Time: O(n)
def huffman_decoding(encoded_data, tree):
    decoded_data = ''
    node = tree
    for char in encoded_data:
        if char == '0':
            node = node.left
        elif char == '1':
            node = node.right
        if node and node.char:
            decoded_data += node.char
            node = tree
    return decoded_data

class Test_Huffmane(unittest.TestCase):

    def test_good_rate_compressing(self):
        a_great_sentence = "The bird is the word"
        print('Testing ', a_great_sentence)

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        self.assertEqual(36, sys.getsizeof(int(encoded_data, base=2)) )
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        self.assertEqual('1101001001101101100101010111100001010110000110111001101101100111101011111000', encoded_data)

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        self.assertLess(sys.getsizeof(int(encoded_data, base=2)), sys.getsizeof(decoded_data))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
        self.assertEqual('The bird is the word', decoded_data)

    def test_hight_frequecy(self):
        a_great_sentence = "AaaaaAAAaaaaaaaaa   bbbb"
        print('Testing ', a_great_sentence)
        encoded_data, tree = huffman_encoding(a_great_sentence)
        self.assertEqual(32, sys.getsizeof(int(encoded_data, base=2)) )
        self.assertEqual('011111101101101111111111101001001000000000', encoded_data)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertEqual(73, sys.getsizeof( decoded_data ))
        self.assertEqual('AaaaaAAAaaaaaaaaa   bbbb', decoded_data)

    def test_no_duplication(self):
        a_great_sentence = "ABCDEFGHIJKLMNOPQRSTUVXWY"
        print('Testing ', a_great_sentence)
        encoded_data, tree = huffman_encoding(a_great_sentence)
        self.assertEqual(48, sys.getsizeof(int(encoded_data, base=2)) )
        self.assertEqual('111000111011100111011100011111110001011001110001111001111011100101101110000010000110000011100101100001111001111111100000011110000001011100110111111100011001110000011011101', encoded_data)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertEqual(74, sys.getsizeof( decoded_data ))
        self.assertEqual('ABCDEFGHIJKLMNOPQRSTUVXWY', decoded_data)

if __name__ == "__main__":
    unittest.main()