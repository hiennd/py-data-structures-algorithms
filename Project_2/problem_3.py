import sys
import heapq
class HuffermanNode(object):
    def __init__(self, freq, char = None, left =  None, right = None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    def merge(self, node2):
        if self < node2:
            return HuffermanNode(self.freq + node2.freq, None, self, node2)
        return HuffermanNode(self.freq, None, node2, self)
    def __lt__(self, value):
        return self.freq < value.freq
    def __str__(self):
        if self.char:
            return f'{self.char}:{str(self.freq)}'
        return str(self.freq)
    ## getter and setter omitted
def huffman_encoding(data):
    ## build historgram O(n)
    hist = dict()
    for char in data:
        hist[char] = hist.get(char, 0) + 1
    print(str(hist))
    ## build tree
    hf_heap = [HuffermanNode(v, k) for k, v in hist.items()]
    print('before heapifying:', ', '.join([str(node) for node in hf_heap]))
    heapq.heapify(hf_heap)
    print('after heapifying:', ', '.join([str(node) for node in hf_heap]))
    while len(hf_heap) > 1:
        min_element_1 = heapq.heappop(hf_heap)
        print(f'min_element_1 = {min_element_1}')
        min_element_2 = heapq.heappop(hf_heap)
        print(f'min_element2 = {min_element_2}')
        merged_elment = min_element_1.merge(min_element_2)
        heapq.heappush(hf_heap, merged_elment)
        print('merging heap:', ', '.join([str(node) for node in hf_heap]))

    print('merged heap:', ', '.join([str(node) for node in hf_heap]))
    ## build codes dict:
    codes = dict()
    def code_char(s, hf_node):
        if not hf_node:
            return
        if hf_node.char:
            if not s:
                codes[hf_node.char] = '0'
            else:
                codes[hf_node.char] = s
        code_char(s + '0', hf_node.left)
        code_char(s + '1', hf_node.right)
    code_char('', hf_heap[0])
    ### encoding
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]
    return (encoded_data, hf_heap[0])

def huffman_decoding(data, tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))