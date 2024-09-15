use std::collections::{HashMap, HashSet};
use bitcoin::secp256k1::{Message, Secp256k1};
use bitcoin::util::base58;
use hex;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_transfer() {
        let mut eonix = EonixSmartContract::new(vec![1; 20]);
        let sender = vec![1; 20];
        let recipient = vec![2; 20];
        let amount = 100;

        eonix.transfer(sender.clone(), recipient.clone(), amount);

        assert_eq!(eonix.balance_of(sender), 0);
        assert_eq!(eonix.balance_of(recipient), amount);
    }

    #[test]
    fn test_approve() {
        let mut eonix = EonixSmartContract::new(vec![1; 20]);
        let owner = vec![1; 20];
        let spender = vec![2; 20];
        let amount = 100;

        eonix.approve(owner.clone(), spender.clone(), amount);

        assert_eq!(eonix.allowance(owner, spender), amount);
    }

    #[test]
    fn test_transfer_from() {
        let mut eonix = EonixSmartContract::new(vec![1; 20]);
        let sender = vec![1; 20];
        let recipient = vec![2; 20];
        let amount = 100;

        eonix.approve(sender.clone(), vec![3; 20], amount);
        eonix.transfer_from(sender.clone(), recipient.clone(), amount);

        assert_eq!(eonix.balance_of(sender), 0);
        assert_eq!(eonix.balance_of(recipient), amount);
    }

    #[test]
    fn test_burn() {
        let mut eonix = EonixSmartContract::new(vec![1; 20]);
        let owner = vec![1; 20];
        let amount = 100;

        eonix.burn(owner.clone(), amount);

        assert_eq!(eonix.balance_of(owner), 0);
        assert_eq!(eonix.total_supply(), 0);
    }

    #[test]
    fn test_mint() {
        let mut eonix = EonixSmartContract::new(vec![1; 20]);
        let recipient = vec![1; 20];
        let amount = 100;

        eonix.mint(recipient.clone(), amount);

        assert_eq!(eonix.balance_of(recipient), amount);
        assert_eq!(eonix.total_supply(), amount);
    }
}
