import unittest
from eonix_smart_contracts import EonixSmartContract

class TestEonixSmartContract(unittest.TestCase):
    def setUp(self):
        self.eonix = EonixSmartContract("owner")

    def test_transfer(self):
        sender = "sender"
        recipient = "recipient"
        amount = 100

        self.eonix.transfer(sender, recipient, amount)

        self.assertEqual(self.eonix.balance_of(sender), 0)
        self.assertEqual(self.eonix.balance_of(recipient), amount)

    def test_approve(self):
        owner = "owner"
        spender = "spender"
        amount = 100

        self.eonix.approve(owner, spender, amount)

        self.assertEqual(self.eonix.allowance(owner, spender), amount)

    def test_transfer_from(self):
        sender = "sender"
        recipient = "recipient"
        amount = 100

        self.eonix.approve(sender, "spender", amount)
        self.eonix.transfer_from(sender, recipient, amount)

        self.assertEqual(self.eonix.balance_of(sender), 0)
        self.assertEqual(self.eonix.balance_of(recipient), amount)

    def test_burn(self):
        owner = "owner"
        amount = 100

        self.eonix.burn(owner, amount)

        self.assertEqual(self.eonix.balance_of(owner), 0)
        self.assertEqual(self.eonix.total_supply(), 0)

    def test_mint(self):
        recipient = "recipient"
        amount = 100

        self.eonix.mint(recipient, amount)

        self.assertEqual(self.eonix.balance_of(recipient), amount)
        self.assertEqual(self.eonix.total_supply(), amount)

if __name__ == "__main__":
    unittest.main()
