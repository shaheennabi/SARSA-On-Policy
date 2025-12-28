import numpy as np

class Agent:
    def __init__(self, num_states, num_actions, gamma, alpha):
        self.num_states = num_states
        self.num_actions = num_actions
        self.q_values = np.zeros((num_states, num_actions))
        self.gamma = gamma 
        self.alpha = alpha 
        


    def update(self, s, a, reward, s_prime, a_prime,):
        current_val = self.q_values[s,a]
        next_val = self.q_values[s_prime, a_prime]

        target = reward + self.gamma * next_val
        td_error = target - current_val

        self.q_values[s,a] += td_error*self.alpha

    