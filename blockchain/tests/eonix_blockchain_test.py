import unittest
from eonix_blockchain import EonixBlockchain, Block, Transaction

class TestEonixBlockchain(unittest.TestCase):
    def test_new_eonix_blockchain(self):
        bc = EonixBlockchain()
        self.assertIsNotNone(bc.db)
        self.assertEqual(len(bc.chain), 0)

    def test_genesis_block(self):
        bc = EonixBlockchain()
        genesis = bc.create_genesis_block()
        self.assertIsNotNone(genesis)
        self.assertEqual(genesis.index, 0)
        self.assertEqual(genesis.previous_hash, "0")
        self.assertEqual(genesis.timestamp, 1643723400)
        self.assertEqual(len(genesis.transactions), 0)

    def test_add_block(self):
        bc = EonixBlockchain()
        genesis = bc.create_genesis_block()
        bc.add_block(genesis)
        self.assertEqual(len(bc.chain), 1)
        self.assertEqual(bc.chain[0].hash, genesis.hash)

    def test_get_block(self):
        bc = EonixBlockchain()
        genesis = bc.create_genesis_block()
        bc.add_block(genesis)
        block = bc.get_block(0)
        self.assertIsNotNone(block)
        self.assertEqual(block.hash, genesis.hash)

    def test_transaction(self):
        tx = Transaction("tx1", 1643723400, "sender1", "recipient1", 10.0)
        self.assertIsNotNone(tx)
        self.assertEqual(tx.id, "tx1")

    def test_block(self):
        block = Block(1, "prev_hash", 1643723401, [])
        self.assertIsNotNone(block)
        self.assertEqual(block.index, 1)

if __name__ == "__main__":
    unittest.main()
