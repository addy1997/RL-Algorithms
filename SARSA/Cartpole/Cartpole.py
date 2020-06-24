import gym
from SARSA_agent import *
import numpy as np
import tensorflow 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
import plotly.express as px

#creating the environment for cartpole system
env = gym.make('CartPole-v0')
seeding = 456
env.seed(seeding)
np.random.seed(seeding)

#agent's observation space and action space
states = env.observation_space.shape[0]
actions = env.action_space.n

#neural network for cartpole-v0 agent
def agent(states, actions):
    """
    creating a DNN using keras
    """
    model = Sequential()
    model.add(Flatten(input_shape=(1, states)))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model

#getting the model ready
model = agent(states, actions)

#defining the SRASA agent
sarsa = SARSAAgent(model=model, nb_actions=actions, policy=EpsGreedyQpolicy())

#compiling the model
sarsa.compile('adam', metrics=['mse', 'accuracy'])

#Training the agent for 30000 steps
sarsa.fit(env, nb_steps=30000, visualize=False, verbose=1)

#testing the model for first 200 episodes
scores = sarsa.test(env, nb_episodes = 200, visualize=False)

#plotting and visualisation 
episode_rewards = scores.history
fig = px.line(episode_rewards, x="Episode", y ="Testing total reward", title='Total rewards over all episodes in testing')
fig.show()

#retaining the action probabilities 
q_values = np.array(sarsa.q_values)
print("the action probabilities are", q_values)

#saving the weights
sarsa.save_weights('sarsa_{}_weights.h5f'.format(env), overwrite=True)







