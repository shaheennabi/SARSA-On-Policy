
import numpy as np


def epsilon_greedy_policy(q_values_of_state, epsilon):

    ## epsilon_greedy
    if np.random.rand() < epsilon:
        return np.random.randint(len(q_values_of_state))
    
    ## total greedy-policy
    else:
        max_q = max(q_values_of_state)
        best_actions = np.where(q_values_of_state ==  max_q)[0]
        return np.random.choice(best_actions)