import json
from websocket import create_connection
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class InteroperabilityFramework:
    def __init__(self, blockchain_networks, traditional_systems, iot_devices):
        self.blockchain_networks = blockchain_networks
        self.traditional_systems = traditional_systems
        self.iot_devices = iot_devices
        self.websocket_connections = {}

    def establish_connections(self):
        for blockchain_network in self.blockchain_networks:
            self.websocket_connections[blockchain_network] = create_connection(f"wss://{blockchain_network}.com/ws")
        for traditional_system in self.traditional_systems:
            self.websocket_connections[traditional_system] = create_connection(f"wss://{traditional_system}.com/ws")
        for iot_device in self.iot_devices:
            self.websocket_connections[iot_device] = create_connection(f"wss://{iot_device}.com/ws")

    def send_message(self, message, destination):
        if destination in self.websocket_connections:
            self.websocket_connections[destination].send(json.dumps(message))
        else:
            print(f"Error: Destination {destination} not found")

    def receive_message(self, source):
        if source in self.websocket_connections:
            message = self.websocket_connections[source].recv()
            return json.loads(message)
        else:
            print(f"Error: Source {source} not found")

    def encrypt_message(self, message, public_key):
        encrypted_message = public_key.encrypt(message.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        return encrypted_message

    def decrypt_message(self, encrypted_message, private_key):
        decrypted_message = private_key.decrypt(encrypted_message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        return decrypted_message.decode()

if __name__ == "__main__":
    blockchain_networks = ["Eonix", "Ethereum", "Bitcoin"]
    traditional_systems = ["SWIFT", "FedWire"]
    iot_devices = ["Device 1", "Device 2"]
    interoperability_framework = InteroperabilityFramework(blockchain_networks, traditional_systems, iot_devices)
    interoperability_framework.establish_connections()

    # Send a message from Eonix to SWIFT
    message = {"amount": 100, "currency": "USD"}
    public_key = serialization.load_pem_public_key(b"public_key.pem", backend=default_backend())
    encrypted_message = interoperability_framework.encrypt_message(message, public_key)
    interoperability_framework.send_message(encrypted_message, "SWIFT")

    # Receive a message from FedWire
    message = interoperability_framework.receive_message("FedWire")
    private_key = serialization.load_pem_private_key(b"private_key.pem", password=None, backend=default_backend())
    decrypted_message = interoperability_framework.decrypt_message(message, private_key)
    print("Received message:", decrypted_message)
