# Problem Statement
In this problem, you will train a simple Q-learning agent from scratch using the Gymnasium environment. The goal is to implement a Q-learning algorithm that allows an agent to learn and improve its performance through interactions with the CartPole-v1 environment.

### You will:
- Set up the Gymnasium environment.
- Implement the Q-learning algorithm.
- Train the Q-learning agent.
- Evaluate the agent's performance.

### Methods to Use:
- Gymnasium Environment: Set up and use the CartPole-v1 environment.
- Q-Learning Algorithm: Implement the Q-learning algorithm, which involves updating a Q-table based on the agent's experiences.
- State Discretization: Discretize the continuous state space into a finite set of discrete states.
- Training Loop: Train the Q-learning agent over multiple episodes, updating the Q-table based on the rewards received.
- Evaluation: Evaluate the performance of the trained agent by measuring its average reward over a set of episodes.

### Exercise Steps:
- Set Up the Gymnasium Environment: Initialize the CartPole-v1 environment.
- Define the state space and action space.
- Initialize the Q-table with zeros.
- Define the hyperparameters: learning rate (alpha), discount factor (gamma), exploration rate (epsilon), and exploration decay rate.
- Create a function to discretize the continuous state space into discrete bins.
- Implement the training loop where the agent interacts with the environment, updates the Q-table, and decays the exploration rate.
- Measure the agent's performance by calculating the average reward over a set of evaluation episodes.