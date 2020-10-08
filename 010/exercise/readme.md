# Problem Statement

The aim of the exercise is to implement k-NN from scratch.
The basic implementation is done for understanding.

# Objective

To understand how kNN works internally.

# Task

- Extend the algorithm for Distance-weighted kNN classification using appropriate dataset.
- Extend the algorithm for regression using appropriate dataset.
- Extend the algorithm with appropriate dataset.
- Implementing KD trees to understand information retrieval. Visit [this](https://www.analyticsvidhya.com/blog/2017/11/information-retrieval-using-kdtree/) site for dataset and references.

# k-NN Algorithm

K-nearest neighbors (KNN) algorithm is a type of supervised ML algorithm which can be used for both classification as well as regression predictive problems.
The following two properties would define KNN
well −
- Lazy learning algorithm − KNN is a lazy learning algorithm because it does not have a specialized training phase and uses all the data for training while classification.
- Non-parametric learning algorithm − KNN is also a non-parametric learning algorithm because it doesn’t assume anything about the underlying data.

K-nearest neighbors (KNN) algorithm uses ‘feature similarity’ to predict the values of new datapoints which further means that the new data point will be assigned a value based on how closely it matches the points in the training set.

1. Load the data
2. Initialize K to your chosen number of neighbors
3. For each example in the data
   - Calculate the distance between the query example and the current example from the data. 
   - Add the distance and the index of the example to an ordered collection
4. Sort the ordered collection of distances and indices from smallest to largest (in ascending order) by the distances
5. Pick the first K entries from the sorted collection 6. Get the labels of the selected K entries
6. If regression, return the mean of the K labels
7. If classification, return the mode of the K labels

Here is a template notebook to get you started:

`knn_starter_exercise.ipynb`

[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gimseng/99-ML-Learning-Projects/blob/master/010/exercise/knn_starter_exercise.ipynb)
[![View in nbviewer](https://github.com/jupyter/design/blob/master/logos/Badges/nbviewer_badge.svg)](https://colab.research.google.com/github/gimseng/99-ML-Learning-Projects/blob/master/010/exercise/knn_starter_exercise.ipynb)


### References
- https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_knn_algorithm_finding_nearest_neighbors.htm
