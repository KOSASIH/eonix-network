import hashlib
import ecdsa

def generate_key_pair():
    private_key = ecdsa.SigningKey.from_secret_exponent(1, curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key.to_string(), public_key.to_string()

def get_address_from_public_key(public_key):
    public_key_bytes = public_key.to_string()
    hash = hashlib.sha3_256(public_key_bytes[1:]).digest()
    address = "0x" + hash.hex()[24:]
    return address

def get_address_from_private_key(private_key):
    public_key = private_key.get_verifying_key()
    return get_address_from_public_key(public_key)

def sign(private_key, message):
    private_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    message = hashlib.sha3_256(message).digest()
    signature = private_key.sign(message)
    return signature

def verify(public_key, message, signature):
    public_key = ecdsa.VerifyingKey.from_string(public_key, curve=ecdsa.SECP256k1)
    message = hashlib.sha3_256(message).digest()
    return public_key.verify(signature, message)
