import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

 class GenerativeAI:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.dataset = pd.read_csv(dataset_path)
        self.scaler = MinMaxScaler()
        self.model = self.create_model()

    def create_model(self):
        model = keras.Sequential([
            keras.layers.Dense(64, activation="relu", input_shape=(self.dataset.shape[1],)),
            keras.layers.Dense(32, activation="relu"),
            keras.layers.Dense(1)
        ])
        model.compile(optimizer="adam", loss="mean_squared_error")
        return model

    def train_model(self, epochs=100):
        self.model.fit(self.scaler.fit_transform(self.dataset), epochs=epochs)

    def generate_data(self, input_data):
        input_data_scaled = self.scaler.transform(input_data)
        generated_data = self.model.predict(input_data_scaled)
        return generated_data

if __name__ == "__main__":
    generative_ai = GenerativeAI("eonix_network_data.csv")
    generative_ai.train_model()
    generated_data = generative_ai.generate_data([[1, 2, 3, 4, 5]])
    print(generated_data)
