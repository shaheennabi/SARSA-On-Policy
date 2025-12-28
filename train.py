
from env import Environment
from agent import Agent
from policy import epsilon_greedy_policy
from config import EPSILON, GAMMA, ALPHA


def train_sarsa(iterations, rows, cols, num_actions):
    num_states = rows * cols
    env = Environment(rows=rows, cols=cols)
    agent = Agent(num_states=num_states, num_actions=num_actions, gamma=GAMMA, alpha=ALPHA)

    for _ in range(iterations):

        state = env.reset()

        action = epsilon_greedy_policy(agent.q_values[state], EPSILON)
        done = False

        while not done: 
            next_state, reward, done = env.step(action)
            next_action = epsilon_greedy_policy(agent.q_values[next_state], EPSILON)
            agent.update(state, action, reward, next_state, next_action)


            state = next_state
            action = next_action

    return agent
