import gym
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

class ReinforcementLearning:
    def __init__(self, environment_name):
        self.environment_name = environment_name
        self.environment = gym.make(environment_name)
        self.scaler = MinMaxScaler()
        self.model = self.create_model()

    def create_model(self):
        model = keras.Sequential([
            keras.layers.Dense(64, activation="relu", input_shape=(self.environment.observation_space.shape[0],)),
            keras.layers.Dense(32, activation="relu"),
            keras.layers.Dense(self.environment.action_space.n)
        ])
        model.compile(optimizer="adam", loss="mean_squared_error")
        return model

    def train_model(self, epochs=100):
        for episode in range(epochs):
            state = self.environment.reset()
            done = False
            rewards = 0
            while not done:
                action = self.model.predict(state)
                next_state, reward, done, _ = self.environment.step(action)
                rewards += reward
                state = next_state
            print(f"Episode {episode+1}, Reward: {rewards}")

    def make_decision(self, state):
        action = self.model.predict(state)
        return action

if __name__ == "__main__":
    reinforcement_learning = ReinforcementLearning("CartPole-v1")
    reinforcement_learning.train_model()
    state = reinforcement_learning.environment.reset()
    action = reinforcement_learning.make_decision(state)
    print(action)
