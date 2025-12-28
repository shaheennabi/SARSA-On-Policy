# SARSA from Scratch (Model-Free Reinforcement Learning)

This repository contains a **from-scratch, modular implementation of SARSA**  
(State–Action–Reward–State–Action), an **on-policy, model-free reinforcement learning**  
algorithm, implemented on a custom **GridWorld environment built without any pre-made RL libraries**.

The focus of this project is **algorithmic clarity and correct temporal logic**, not performance or framework usage.

---

## Why this project

Many reinforcement learning examples:
- rely on Gym or pre-built environments
- hide the learning loop behind abstractions
- blur the distinction between policy and value learning

This project does the opposite:
- the environment is implemented manually
- the SARSA update is written explicitly
- the policy is separate and stateless
- the training loop shows the full `(s, a, r, s', a')` flow

The goal is to **understand model-free control from first principles**.

---

## What SARSA is (core idea)

SARSA is an **on-policy temporal-difference control algorithm**.  
It learns the value of **the actions the agent actually takes**, not the actions that would be optimal under a greedy policy.

At each step, SARSA updates the value of the **current state–action pair** using the value of the **next state–action pair chosen by the same policy**.

This single detail is the defining difference between SARSA and Q-learning.

---

## SARSA update rule

For a transition:  
(s, a) → r → (s', a')

```math
Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma Q(s', a') - Q(s, a) \right]


### SARSA update rule (continued)

Where:
- **α** is the learning rate
- **γ** is the discount factor
- **a'** is chosen using the **same policy** as **a**

Because the next action comes from the same policy, SARSA is **on-policy**.

---

## How to run

### Installation

Install the only required dependency:

```bash
pip install numpy

(Optional: use a virtual environment for isolation)

```bash
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
pip install numpy


No other external libraries or RL frameworks are needed.

### Running the training

Execute the main training script:

```bash
python train.py

You can customize hyperparameters directly in `train.py` or by modifying the `train_sarsa` function call (e.g., number of episodes, grid size, learning rate, etc.).

### Expected behavior after training

- Q-values near the terminal state (bottom-right corner) should be close to 0
- States farther from the terminal should have increasingly negative Q-values
- Optimal action-values should propagate backward from the goal over episodes
- The agent learns a near-optimal policy avoiding long paths due to the -1 step penalty

Training typically converges well within 10,000–20,000 episodes on the default 5×5 grid.

### Repository structure
.
├── env.py          # GridWorld environment (dynamics only)
├── agent.py        # SARSA agent (Q-table + update rule)
├── policy.py       # ε-greedy policy with decay
├── train.py        # Training loop and execution entry point
├── README.md       # This file
└── requirements.txt # (optional) lists numpy



### Notes

This implementation emphasizes:

- Temporal correctness in the SARSA loop
- Clear separation of environment, agent, and policy
- Explicit handling of the (s, a, r, s', a') tuple

It serves as a clean foundation for understanding on-policy control and can be extended to Q-learning, Expected SARSA, or more advanced methods.