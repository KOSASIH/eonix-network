import hashlib
import json

class EonixSmartContract:
    def __init__(self, owner):
        self.owner = owner
        self.balances = {owner: 100000000 * (10 ** 18)}
        self.allowances = {}
        self.token_holders = set([owner])
        self.token_balances = {owner: 100000000 * (10 ** 18)}
        self.token_allowances = {}
        self.total_supply = 100000000 * (10 ** 18)
        self.name = "Eonix Token"
        self.symbol = "EON"
        self.decimals = 18

    def transfer(self, sender, recipient, amount):
        if self.balances.get(sender, 0) < amount:
            raise ValueError("Insufficient balance")
        self.balances[sender] -= amount
        self.balances[recipient] = self.balances.get(recipient, 0) + amount
        self.emit_transfer(sender, recipient, amount)

    def approve(self, owner, spender, amount):
        self.allowances.setdefault(owner, {})[spender] = amount
        self.emit_approval(owner, spender, amount)

    def transfer_from(self, sender, recipient, amount):
        if self.allowances.get(sender, {}).get(self.owner, 0) < amount:
            raise ValueError("Insufficient allowance")
        if self.balances.get(sender, 0) < amount:
            raise ValueError("Insufficient balance")
        self.balances[sender] -= amount
        self.balances[recipient] = self.balances.get(recipient, 0) + amount
        self.emit_transfer(sender, recipient, amount)

    def burn(self, owner, amount):
        if self.balances.get(owner, 0) < amount:
            raise ValueError("Insufficient balance")
        self.balances[owner] -= amount
        self.total_supply -= amount
        self.emit_burn(owner, amount)

    def mint(self, recipient, amount):
        if self.owner != self.owner:
            raise ValueError("Only the owner can mint tokens")
        self.total_supply += amount
        self.balances[recipient] = self.balances.get(recipient, 0) + amount
        self.emit_mint(recipient, amount)

    def balance_of(self, user):
        return self.balances.get(user, 0)

    def allowance(self, owner, spender):
        return self.allowances.get(owner, {}).get(spender, 0)

    def total_supply(self):
        return self.total_supply

    def emit_transfer(self, from_address, to_address, value):
        print(f"Transfer({from_address}, {to_address}, {value})")

    def emit_approval(self, owner, spender, value):
        print(f"Approval({owner}, {spender}, {value})")

    def emit_burn(self, owner, value):
        print(f"Burn({owner}, {value})")

    def emit_mint(self, recipient, value):
        print(f"Mint({recipient}, {value})")
