import unittest
from eonix_utils import generate_key_pair, get_address_from_public_key, get_address_from_private_key, sign, verify

class TestEonixUtils(unittest.TestCase):
    def test_generate_key_pair(self):
        private_key, public_key = generate_key_pair()
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)

    def test_get_address_from_public_key(self):
        private_key, public_key = generate_key_pair()
        address = get_address_from_public_key(public_key)
        self.assertIsNotNone(address)

    def test_get_address_from_private_key(self):
        private_key, _ = generate_key_pair()
        address = get_address_from_private_key(private_key)
        self.assertIsNotNone(address)

    def test_sign(self):
        private_key, _ = generate_key_pair()
        message = b"Hello, World!"
        signature = sign(private_key, message)
        self.assertIsNotNone(signature)

    def test_verify(self):
        private_key, public_key = generate_key_pair()
        message = b"Hello, World!"
        signature = sign(private_key, message)
        self.assertTrue(verify(public_key, message, signature))

if __name__ == "__main__":
    unittest.main()
