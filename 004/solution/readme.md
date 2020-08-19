# My Solution

In this folder, you will find the following jupyter notebook using a simple LSTM neural network for text generation: 

`text_generation_model.ipynb`

[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gimseng/99-ML-Learning-Projects/blob/master/004/solution/text_generation_model.ipynb)
[![View in nbviewer](https://github.com/jupyter/design/blob/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/gimseng/99-ML-Learning-Projects/blob/master/004/solution/text_generation_model.ipynb)

The first part of the notebook consists of tokenization of the text. 

This is followed by constructing a six-layer simple neural network using `TensorFlow`, consisting of an embedding layer, a bidirectional LSTM layer, a dropout layer, a LSTM layer and finally two standard neural network layer. 

After training, you will find a seed text `I really like the Arctic Monkeys and ` as input to the trained network to produce new lyrics.
