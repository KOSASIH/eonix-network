use std::collections::{HashMap, HashSet};
use std::sync::{Arc, Mutex};
use bitcoin::secp256k1::{Message, Secp256k1};
use bitcoin::util::base58;
use hex;

pub struct EonixSmartContract {
    owner: Vec<u8>,
    balances: HashMap<Vec<u8>, u64>,
    allowances: HashMap<Vec<u8>, HashMap<Vec<u8>, u64>>,
    token_holders: HashSet<Vec<u8>>,
    token_balances: HashMap<Vec<u8>, u64>,
    token_allowances: HashMap<Vec<u8>, HashMap<Vec<u8>, u64>>,
    total_supply: u64,
    name: String,
    symbol: String,
    decimals: u8,
}

impl EonixSmartContract {
    pub fn new(owner: Vec<u8>) -> Self {
        EonixSmartContract {
            owner,
            balances: HashMap::new(),
            allowances: HashMap::new(),
            token_holders: HashSet::new(),
            token_balances: HashMap::new(),
            token_allowances: HashMap::new(),
            total_supply: 100000000 * (10 as u64).pow(18 as u32),
            name: "Eonix Token".to_string(),
            symbol: "EON".to_string(),
            decimals: 18,
        }
    }

    pub fn transfer(&mut self, sender: Vec<u8>, recipient: Vec<u8>, amount: u64) {
        if self.balances.get(&sender).unwrap_or(&0) < &amount {
            panic!("Insufficient balance");
        }
        self.balances.insert(sender.clone(), self.balances.get(&sender).unwrap_or(&0) - amount);
        self.balances.insert(recipient.clone(), self.balances.get(&recipient).unwrap_or(&0) + amount);
        self.emit_transfer(sender, recipient, amount);
    }

    pub fn approve(&mut self, owner: Vec<u8>, spender: Vec<u8>, amount: u64) {
        self.allowances
            .entry(owner.clone())
            .or_insert(HashMap::new())
            .insert(spender.clone(), amount);
        self.emit_approval(owner, spender, amount);
    }

    pub fn transfer_from(&mut self, sender: Vec<u8>, recipient: Vec<u8>, amount: u64) {
        if self.allowances
            .get(&sender)
            .and_then(|allowances| allowances.get(&self.owner))
            .unwrap_or(&0) < &amount
        {
            panic!("Insufficient allowance");
        }
        if self.balances.get(&sender).unwrap_or(&0) < &amount {
            panic!("Insufficient balance");
        }
        self.balances.insert(sender.clone(), self.balances.get(&sender).unwrap_or(&0) - amount);
        self.balances.insert(recipient.clone(), self.balances.get(&recipient).unwrap_or(&0) + amount);
        self.emit_transfer(sender, recipient, amount);
    }

    pub fn burn(&mut self, owner: Vec<u8>, amount: u64) {
        if self.balances.get(&owner).unwrap_or(&0) < &amount {
            panic!("Insufficient balance");
        }
        self.balances.insert(owner.clone(), self.balances.get(&owner).unwrap_or(&0) - amount);
        self.total_supply -= amount;
        self.emit_burn(owner, amount);
    }

    pub fn mint(&mut self, recipient: Vec<u8>, amount: u64) {
        if self.owner != self.owner {
            panic!("Only the owner can mint tokens");
        }
        self.total_supply += amount;
        self.balances.insert(recipient.clone(), self.balances.get(&recipient).unwrap_or(&0) + amount);
        self.emit_mint(recipient, amount);
    }

    pub fn balance_of(&self, user: Vec<u8>) -> u64 {
        self.balances.get(&user).unwrap_or(&0).clone()
    }

    pub fn allowance(&self, owner: Vec<u8>, spender: Vec<u8>) -> u64 {
        self.allowances
            .get(&owner)
            .and_then(|allowances| allowances.get(&spender))
            .unwrap_or(&0)
            .clone()
    }

    pub fn total_supply(&self) -> u64 {
        self.total_supply
    }

    fn emit_transfer(&self, from: Vec<u8>, to: Vec<u8>, value: u64) {
        println!("Transfer({:?}, {:?}, {})", from, to, value);
    }

    fn emit_approval(&self, owner: Vec<u8>, spender: Vec<u8>, value: u64) {
        println!("Approval({:?}, {:?}, {})", owner, spender, value);
    }

    fn emit_burn(&self, owner: Vec<u8>, value: u64) {
        println!("Burn({:?}, {})", owner, value);
    }

    fn emit_mint(&self, recipient: Vec<u8>, value: u64) {
        println!("Mint({:?}, {})", recipient, value);
    }
}
