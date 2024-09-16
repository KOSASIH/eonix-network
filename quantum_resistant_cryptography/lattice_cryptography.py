import numpy as np
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class LatticeCryptography:
    def __init__(self, n, q, sigma):
        self.n = n
        self.q = q
        self.sigma = sigma
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()

    def generate_private_key(self):
        private_key = np.random.randint(-self.sigma, self.sigma, size=self.n)
        return private_key

    def generate_public_key(self):
        public_key = np.random.randint(0, self.q, size=self.n)
        return public_key

    def encrypt(self, message):
        encrypted_message = np.dot(message, self.public_key) % self.q
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = np.dot(encrypted_message, self.private_key) % self.q
        return decrypted_message

    def serialize_public_key(self):
        public_key_pem = self.public_key.tobytes()
        return public_key_pem

    def deserialize_public_key(self, public_key_pem):
        public_key = np.frombuffer(public_key_pem, dtype=np.int64)
        return public_key

if __name__ == "__main__":
    lattice_cryptography = LatticeCryptography(n=1024, q=12289, sigma=3)
    message = np.array([1, 2, 3, 4, 5])
    encrypted_message = lattice_cryptography.encrypt(message)
    decrypted_message = lattice_cryptography.decrypt(encrypted_message)
    print("Original message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)
