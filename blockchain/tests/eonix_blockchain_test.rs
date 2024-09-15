use std::sync::{Arc, Mutex};

use bitcoin::secp256k1::{Message, Secp256k1};
use bitcoin::util::base58;
use hex;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_eonix_blockchain() {
        let bc = EonixBlockchain::new();
        assert!(bc.db.lock().unwrap().is_empty());
        assert!(bc.chain.is_empty());
    }

    #[test]
    fn test_genesis_block() {
        let bc = EonixBlockchain::new();
        let genesis = bc.genesis_block().clone();
        assert_eq!(genesis.index, 0);
        assert_eq!(genesis.previous_hash, "0");
        assert_eq!(genesis.timestamp, 1643723400);
        assert!(genesis.transactions.is_empty());
    }

    #[test]
    fn test_add_block() {
        let mut bc = EonixBlockchain::new();
        let genesis = bc.genesis_block().clone();
        bc.add_block(genesis.clone());
        assert_eq!(bc.chain.len(), 1);
        assert_eq!(bc.chain[0].hash, genesis.hash);
    }

    #[test]
    fn test_get_block() {
        let mut bc = EonixBlockchain::new();
        let genesis = bc.genesis_block().clone();
        bc.add_block(genesis.clone());
        let block = bc.get_block(0).unwrap();
        assert_eq!(block.hash, genesis.hash);
    }

    #[test]
    fn test_transaction() {
        let tx = Transaction {
            id: "tx1".to_string(),
            timestamp: 1643723400,
            sender: "sender1".to_string(),
            recipient: "recipient1".to_string(),
            amount: 10.0,
        };
        assert!(tx.id == "tx1");
    }

    #[test]
    fn test_block() {
        let block = Block {
            index: 1,
            previous_hash: "prev_hash".to_string(),
            timestamp: 1643723401,
            transactions: Vec::new(),
            hash: "".to_string(),
        };
        assert!(block.index == 1);
    }
}
