import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.cluster import KMeans

class NodeClustering:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.dataset = pd.read_csv(dataset_path)
        self.model = self.create_model()

    def create_model(self):
        model = keras.Sequential([
            keras.layers.Dense(64, activation="relu", input_shape=(self.dataset.shape[1],)),
            keras.layers.Dense(32, activation="relu"),
            keras.layers.Dense(8)
        ])
        model.compile(optimizer="adam", loss="mean_squared_error")
        return model

    def train_model(self, epochs=100):
        self.model.fit(self.dataset, epochs=epochs)

    def cluster_nodes(self, input_data):
        predictions = self.model.predict(input_data)
        kmeans = KMeans(n_clusters=8)
        kmeans.fit(predictions)
        return kmeans.labels_

if __name__ == "__main__":
    node_clustering = NodeClustering("eonix_network_data.csv")
    node_clustering.train_model()
    input_data = [[1, 2, 3, 4, 5]]
    node_labels = node_clustering.cluster_nodes(input_data)
    print(node_labels)
