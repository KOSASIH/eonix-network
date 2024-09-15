use bitcoin::secp256k1::{Message, Secp256k1};
use bitcoin::util::base58;
use hex;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_generate_key_pair() {
        let (private_key, public_key) = generate_key_pair();
        assert!(private_key.len() > 0);
        assert!(public_key.len() > 0);
    }

    #[test]
    fn test_get_address_from_public_key() {
        let (private_key, public_key) = generate_key_pair();
        let address = get_address_from_public_key(&public_key);
        assert!(address.len() > 0);
    }

    #[test]
    fn test_get_address_from_private_key() {
        let (private_key, _) = generate_key_pair();
        let address = get_address_from_private_key(&private_key);
        assert!(address.len() > 0);
    }

    #[test]
    fn test_sign() {
        let (private_key, _) = generate_key_pair();
        let message = b"Hello, World!";
        let signature = sign(&private_key, message);
        assert!(signature.len() > 0);
    }

    #[test]
    fn test_verify() {
        let (private_key, public_key) = generate_key_pair();
        let message = b"Hello, World!";
        let signature = sign(&private_key, message);
        assert!(verify(&public_key, message, &signature));
    }
}
