import numpy as np
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class CodeCryptography:
    def __init__(self, n, k, t):
        self.n = n
        self.k = k
        self.t = t
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()

    def generate_private_key(self):
        private_key = np.random.randint(0, 2, size=self.k)
        return private_key

    def generate_public_key(self):
        public_key = np.random.randint(0, 2, size=self.n)
        return public_key

    def encrypt(self, message):
        encrypted_message = np.dot(message, self.public_key) % 2
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = np.dot(encrypted_message, self.private_key) % 2
        return decrypted_message

    def serialize_public_key(self):
        public_key_pem = self.public_key.tobytes()
        return public_key_pem

    def deserialize_public_key(self, public_key_pem):
        public_key = np.frombuffer(public_key_pem, dtype=np.int64)
        return public_key

if __name__ == "__main__":
    code_cryptography = CodeCryptography(n=1024, k=512, t=50)
    message = np.array([1, 0, 1, 0, 1])
    encrypted_message = code_cryptography.encrypt(message)
    decrypted_message = code_cryptography.decrypt(encrypted_message)
    print("Original message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)
