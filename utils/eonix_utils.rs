use bitcoin::secp256k1::{Message, Secp256k1};
use bitcoin::util::base58;
use hex;

pub fn generate_key_pair() -> (Vec<u8>, Vec<u8>) {
    let secp = Secp256k1::new();
    let (private_key, public_key) = secp.generate_keypair(&mut rand::thread_rng());
    (private_key.to_vec(), public_key.to_vec())
}

pub fn get_address_from_public_key(public_key: &[u8]) -> String {
    let public_key = bitcoin::PublicKey::from_slice(public_key).unwrap();
    let address = bitcoin::Address::p2pkh(&public_key, bitcoin::Network::Bitcoin).unwrap();
    address.to_string()
}

pub fn get_address_from_private_key(private_key: &[u8]) -> String {
    let private_key = bitcoin::PrivateKey::from_slice(private_key).unwrap();
    let public_key = private_key.public_key();
    get_address_from_public_key(&public_key.to_vec())
}

pub fn sign(private_key: &[u8], message: &[u8]) -> Vec<u8> {
    let secp = Secp256k1::new();
    let private_key = bitcoin::PrivateKey::from_slice(private_key).unwrap();
    let message = Message::from_slice(message).unwrap();
    let signature = secp.sign(&private_key, &message).unwrap();
    signature.to_vec()
}

pub fn verify(public_key: &[u8], message: &[u8], signature: &[u8]) -> bool {
    let secp = Secp256k1::new();
    let public_key = bitcoin::PublicKey::from_slice(public_key).unwrap();
    let message = Message::from_slice(message).unwrap();
    let signature = bitcoin::Signature::from_slice(signature).unwrap();
    secp.verify(&public_key, &message, &signature).is_ok()
}
