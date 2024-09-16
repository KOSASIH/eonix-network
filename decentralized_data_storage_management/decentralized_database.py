import sqlite3

class DecentralizedDatabase:
    def __init__(self, database_url):
        self.database_url = database_url
        self.connection = sqlite3.connect(self.database_url)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        # Create a table in the decentralized database
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})")
        self.connection.commit()

    def insert_data(self, table_name, data):
        # Insert data into the decentralized database
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(data))})", data)
        self.connection.commit()

    def retrieve_data(self, table_name, key):
        # Retrieve data from the decentralized database
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE key = ?", key)
        return self.cursor.fetchone()

if __name__ == "__main__":
    database_url = "sqlite:///decentralized_database.db"
    decentralized_database = DecentralizedDatabase(database_url)

    # Create a table in the decentralized database
    table_name = "metadata"
    columns = ["key", "value"]
    decentralized_database.create_table(table_name, columns)

    # Insert data into the decentralized database
    data = ("key", "value")
    decentralized_database.insert_data(table_name, data)

    # Retrieve data from the decentralized database
    retrieved_data = decentralized_database.retrieve_data(table_name, "key")
    print("Retrieved Data:", retrieved_data)
