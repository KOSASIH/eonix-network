import ipfshttpclient
from sqlalchemy import create_engine

class DecentralizedDataStorage:
    def __init__(self, ipfs_api, database_url):
        self.ipfs_api = ipfs_api
        self.database_url = database_url
        self.ipfs_client = ipfshttpclient.connect(self.ipfs_api)
        self.database_engine = create_engine(self.database_url)

    def store_data(self, data):
        # Store data in IPFS
        ipfs_hash = self.ipfs_client.add_bytes(data)
        return ipfs_hash

    def retrieve_data(self, ipfs_hash):
        # Retrieve data from IPFS
        data = self.ipfs_client.cat(ipfs_hash)
        return data

    def store_metadata(self, metadata):
        # Store metadata in decentralized database
        self.database_engine.execute("INSERT INTO metadata (key, value) VALUES (?, ?)", metadata)

    def retrieve_metadata(self, key):
        # Retrieve metadata from decentralized database
        result = self.database_engine.execute("SELECT value FROM metadata WHERE key = ?", key)
        return result.fetchone()[0]

if __name__ == "__main__":
    ipfs_api = "http://localhost:5001"
    database_url = "sqlite:///decentralized_database.db"
    decentralized_data_storage = DecentralizedDataStorage(ipfs_api, database_url)

    # Store data in IPFS
    data = b"Hello, World!"
    ipfs_hash = decentralized_data_storage.store_data(data)
    print("IPFS Hash:", ipfs_hash)

    # Retrieve data from IPFS
    retrieved_data = decentralized_data_storage.retrieve_data(ipfs_hash)
    print("Retrieved Data:", retrieved_data)

    # Store metadata in decentralized database
    metadata = ("key", "value")
    decentralized_data_storage.store_metadata(metadata)

    # Retrieve metadata from decentralized database
    retrieved_metadata = decentralized_data_storage.retrieve_metadata("key")
    print("Retrieved Metadata:", retrieved_metadata)
