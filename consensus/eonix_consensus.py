import hashlib
import time
from typing import List, Optional

from eonix_network.blockchain import Blockchain
from eonix_network.crypto import Crypto
from eonix_network.network import Network
from eonix_network.transaction import Transaction

class EonixConsensus:
    def __init__(self, blockchain: Blockchain, network: Network, crypto: Crypto):
        self.blockchain = blockchain
        self.network = network
        self.crypto = crypto
        self.validators = {}
        self.current_block = None

    def add_validator(self, validator: 'Validator'):
        self.validators[validator.public_key] = validator

    def remove_validator(self, public_key: str):
        del self.validators[public_key]

    def create_new_block(self, transactions: List[Transaction]) -> 'Block':
        block = Block(transactions)
        block_hash = self.crypto.hash(block)
        signature = self.crypto.sign(block_hash, self.validators[list(self.validators.keys())[0]].private_key)
        block.signature = signature
        self.blockchain.add_block(block)
        return block

    def verify_block(self, block: 'Block') -> bool:
        block_hash = self.crypto.hash(block)
        return self.crypto.verify(block_hash, block.signature, self.validators[list(self.validators.keys())[0]].public_key)

    def start_consensus(self):
        while True:
            time.sleep(1)
            current_block = self.current_block
            if current_block is None or time.time() - current_block.timestamp > 10:
                transactions = self.network.get_transactions()
                block = self.create_new_block(transactions)
                self.current_block = block

class Validator:
    def __init__(self, public_key: str, private_key: str):
        self.public_key = public_key
        self.private_key = private_key

class Block:
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions
        self.timestamp = time.time()
        self.signature = None

    def __hash__(self):
        return int(hashlib.sha256(str(self.transactions).encode()).hexdigest(), 16)
