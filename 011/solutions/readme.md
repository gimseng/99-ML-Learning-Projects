# My solution

See the following jupyter notebook:

- `q_learning.ipynb`: Jupyter notebook with the implementation of the Q-learning algorithm.

 [![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gimseng/99-ML-Learning-Projects/blob/master/011/solution/q-learning.ipynb)
 [![View in nbviewer](https://github.com/jupyter/design/blob/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/gimseng/99-ML-Learning-Projects/blob/master/011/solution/q-learning.ipynb)

The first part of the notebook initialises the gym environment, q table and training hyperparameters. 

Then, a function is created to discretise the continuous state space into discrete bins. 

Following this, the q table is updated through the training loop. Lastly, the agent is evaluated based on an evaluation run. 