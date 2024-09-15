use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use std::time::{Duration, Instant};

use crate::blockchain::{Block, Blockchain};
use crate::crypto::{Crypto, Hash};
use crate::network::{Network, Transaction};

pub struct EonixConsensus {
    blockchain: Arc<Mutex<Blockchain>>,
    network: Arc<Mutex<Network>>,
    crypto: Arc<Mutex<Crypto>>,
    validators: HashMap<String, Validator>,
    current_block: Option<Block>,
    lock: Mutex<()>,
}

impl EonixConsensus {
    pub fn new(blockchain: Arc<Mutex<Blockchain>>, network: Arc<Mutex<Network>>, crypto: Arc<Mutex<Crypto>>) -> Self {
        EonixConsensus {
            blockchain,
            network,
            crypto,
            validators: HashMap::new(),
            current_block: None,
            lock: Mutex::new(()),
        }
    }

    pub fn add_validator(&mut self, validator: Validator) {
        self.validators.insert(validator.public_key.clone(), validator);
    }

    pub fn remove_validator(&mut self, public_key: &str) {
        self.validators.remove(public_key);
    }

    pub fn create_new_block(&mut self, transactions: Vec<Transaction>) -> Result<Block, String> {
        let block = Block::new(transactions);
        let block_hash = self.crypto.lock().unwrap().hash(&block);
        let signature = self.crypto.lock().unwrap().sign(&block_hash, &self.validators.values().next().unwrap().private_key)?;
        block.signature = signature;
        self.blockchain.lock().unwrap().add_block(block.clone());
        Ok(block)
    }

    pub fn verify_block(&self, block: &Block) -> bool {
        let block_hash = self.crypto.lock().unwrap().hash(block);
        self.crypto.lock().unwrap().verify(&block_hash, &block.signature, &self.validators.values().next().unwrap().public_key)
    }

    pub fn start_consensus(&mut self) {
        let mut interval = tokio::time::interval(Duration::from_secs(1));
        tokio::spawn(async move {
            loop {
                interval.tick().await;
                let current_block = self.current_block.clone();
                if current_block.is_none() || current_block.unwrap().timestamp.elapsed().unwrap().as_secs() > 10 {
                    let transactions = self.network.lock().unwrap().get_transactions();
                    let block = self.create_new_block(transactions).unwrap();
                    self.current_block = Some(block);
                }
            }
        });
    }
}

pub struct Validator {
    public_key: String,
    private_key: String,
}

impl Validator {
    pub fn new(public_key: String, private_key: String) -> Self {
        Validator { public_key, private_key }
    }
}
