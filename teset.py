import gym
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from collections import deque
import random

# Definição do modelo DQN
def build_model(state_size, action_size):
    model = Sequential()
    model.add(Dense(24, input_dim=state_size, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(action_size, activation='linear'))
    model.compile(loss='mse', optimizer=Adam(lr=0.001))
    return model

# Parâmetros do ambiente
env = gym.make('CartPole-v1')
state_size = env.observation_space.shape[0]
action_size = env.action_space.n
model = build_model(state_size, action_size)

# Hiperparâmetros
memory = deque(maxlen=2000)
batch_size = 32
gamma = 0.95  # Fator de desconto
epsilon = 1.0  # Taxa de exploração inicial
epsilon_min = 0.01
epsilon_decay = 0.995
learning_rate = 0.001

# Função para escolher ação
def act(state):
    if np.random.rand() <= epsilon:
        return random.randrange(action_size)
    act_values = model.predict(state)
    return np.argmax(act_values[0])

# Função para treinar o modelo
def replay():
    global epsilon
    if len(memory) < batch_size:
        return
    minibatch = random.sample(memory, batch_size)
    for state, action, reward, next_state, done in minibatch:
        target = reward
        if not done:
            target = (reward + gamma * np.amax(model.predict(next_state)[0]))
        target_f = model.predict(state)
        target_f[0][action] = target
        model.fit(state, target_f, epochs=1, verbose=0)
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Loop de treinamento
episodes = 1000
for e in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    for time in range(500):
        action = act(state)
        next_state, reward, done, _ = env.step(action)
        reward = reward if not done else -10
        next_state = np.reshape(next_state, [1, state_size])
        memory.append((state, action, reward, next_state, done))
        state = next_state
        if done:
            print(f"episode: {e}/{episodes}, score: {time}, e: {epsilon:.2}")
            break
        replay()