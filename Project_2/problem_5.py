import hashlib
from collections import deque
import time
import unittest

class Block(object):
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        return f"{self.timestamp}-{self.data}-{self.previous_hash}"

class BlockChain:
    def __init__(self):
        self.chain = deque()
        genesis_block = Block(time.time(), [], "0")

        self.chain.append(genesis_block)
    
    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        self.chain.append(block)
        return True

    def verify(self):
        previous_hash = '0' ## genesis_block
        for block in self.chain:
            if previous_hash != block.previous_hash:
                print(f'Failed at block {block} != {previous_hash}')
                return False
            previous_hash = block.hash
        return True

class TestAdding(unittest.TestCase):

    def test_adding_invalid_block(self):
        blockchain = BlockChain()
        invalid_block = Block(time.time(), 'Test Invalid Block', 'randome_hash')

        self.assertFalse(blockchain.add_block(invalid_block))
        self.assertTrue(blockchain.verify())

    def test_adding_valid_block(self):
        blockchain = BlockChain()
        block = Block(time.time(), 'Test Valid Block', blockchain.last_block.hash)

        self.assertTrue(blockchain.add_block(block))
        self.assertTrue(blockchain.verify())
    
    def test_verifing(self):
        blockchain = BlockChain()
        previous_hash = blockchain.last_block.hash 
        for i in range(100):
            block = Block(time.time(), 'Test Data' + str(i), previous_hash)
            self.assertTrue(blockchain.add_block(block))
            previous_hash = block.hash
        self.assertTrue(blockchain.verify())

if __name__ == "__main__":
    unittest.main()