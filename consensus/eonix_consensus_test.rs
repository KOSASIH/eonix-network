#[cfg(test)]
mod tests {
    use super::*;
    use crate::eonix_consensus::{EonixConsensus, Validator, Block, Transaction};
    use crate::eonix_crypto::{Crypto, Hash};
    use std::collections::HashMap;

    #[test]
    fn test_add_validator() {
        let mut consensus = EonixConsensus::new(HashMap::new(), vec![]);
        let validator = Validator::new("public_key", "private_key");
        consensus.add_validator(validator.clone());
        assert_eq!(consensus.validators.len(), 1);
        assert_eq!(consensus.validators.get(&validator.public_key).unwrap(), &validator);
    }

    #[test]
    fn test_remove_validator() {
        let mut consensus = EonixConsensus::new(HashMap::new(), vec![]);
        let validator = Validator::new("public_key", "private_key");
        consensus.add_validator(validator.clone());
        consensus.remove_validator(&validator.public_key);
        assert_eq!(consensus.validators.len(), 0);
    }

    #[test]
    fn test_create_new_block() {
        let mut consensus = EonixConsensus::new(HashMap::new(), vec![]);
        let transactions = vec![Transaction::new(), Transaction::new()];
        let block = consensus.create_new_block(transactions).unwrap();
        assert_eq!(block.transactions.len(), 2);
        assert_eq!(block.timestamp, consensus.current_block.as_ref().unwrap().timestamp);
    }

    #[test]
    fn test_verify_block() {
        let mut consensus = EonixConsensus::new(HashMap::new(), vec![]);
        let block = Block::new(vec![Transaction::new(), Transaction::new()]);
        let signature = consensus.crypto.sign(block.hash(), "private_key").unwrap();
        block.signature = signature;
        assert!(consensus.verify_block(&block));
    }

    #[test]
    fn test_start_consensus() {
        let mut consensus = EonixConsensus::new(HashMap::new(), vec![]);
        consensus.start_consensus();
        std::thread::sleep(std::time::Duration::from_secs(2));
        assert!(consensus.current_block.is_some());
    }

    #[bench]
    fn bench_create_new_block(b: &mut Bencher) {
        let mut consensus = EonixConsensus::new(HashMap::new(), vec![]);
        let transactions = vec![Transaction::new(); 100];
        b.iter(|| {
            consensus.create_new_block(transactions.clone()).unwrap();
        });
    }
}
