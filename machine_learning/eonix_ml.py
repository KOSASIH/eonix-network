import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

class EonixML:
    def __init__(self):
        self.model = None

    def load_data(self, file_path):
        data = pd.read_csv(file_path)
        X = data.drop('target', axis=1)
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def create_model(self, input_shape, num_classes):
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=input_shape),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def train_model(self, X_train, y_train, epochs=10):
        self.model.fit(X_train, y_train, epochs=epochs)

    def evaluate_model(self, X_test, y_test):
        loss, accuracy = self.model.evaluate(X_test, y_test)
        return accuracy

    def predict(self, X):
        return self.model.predict(X)

    def save_model(self, file_path):
        self.model.save(file_path)

    def load_model(self, file_path):
        self.model = keras.models.load_model(file_path)

if __name__ == '__main__':
    eonix_ml = EonixML()
    X_train, X_test, y_train, y_test = eonix_ml.load_data('data.csv')
    eonix_ml.create_model((28, 28), 10)
    eonix_ml.train_model(X_train, y_train, epochs=10)
    accuracy = eonix_ml.evaluate_model(X_test, y_test)
    print(f"Model accuracy: {accuracy:.2f}%")
    eonix_ml.save_model('eonix_ml_model.h5')
