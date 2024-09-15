import unittest
from unittest.mock import MagicMock
from eonix_consensus import EonixConsensus, Validator, Block, Transaction
from eonix_crypto import Crypto
import time
import threading

class TestEonixConsensus(unittest.TestCase):
    def test_add_validator(self):
        consensus = EonixConsensus()
        validator = Validator("public_key", "private_key")
        consensus.add_validator(validator)
        self.assertEqual(len(consensus.validators), 1)
        self.assertEqual(consensus.validators["public_key"], validator)

    def test_remove_validator(self):
        consensus = EonixConsensus()
        validator = Validator("public_key", "private_key")
        consensus.add_validator(validator)
        consensus.remove_validator("public_key")
        self.assertEqual(len(consensus.validators), 0)

    def test_create_new_block(self):
        consensus = EonixConsensus()
        transactions = [Transaction(), Transaction()]
        block = consensus.create_new_block(transactions)
        self.assertEqual(len(block.transactions), 2)
        self.assertIsNotNone(block.timestamp)

    def test_verify_block(self):
        consensus = EonixConsensus()
        block = Block([Transaction(), Transaction()])
        signature = consensus.crypto.sign(block.hash(), "private_key")
        block.signature = signature
        self.assertTrue(consensus.verify_block(block))

    def test_start_consensus(self):
        consensus = EonixConsensus()
        consensus.start_consensus()
        time.sleep(2)
        self.assertIsNotNone(consensus.current_block)

    def test_benchmark_create_new_block(self):
        consensus = EonixConsensus()
        transactions = [Transaction() for _ in range(100)]
        start_time = time.time()
        for _ in range(100):
            consensus.create_new_block(transactions)
        end_time = time.time()
        print(f"Time taken to create 100 blocks: {end_time - start_time} seconds")

if __name__ == '__main__':
    unittest.main()
