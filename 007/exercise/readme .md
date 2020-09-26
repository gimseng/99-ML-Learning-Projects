# Exercise 1

* Load the breast cancer dataset using the scikit learn library and split the dataset into train (70%) and test (30%) set. Print test and train set sizes. Also the unique classes.
* Train two DecisionTree classifiers and report the F1 score. Use the information gain for the one classifier and the Gini impurity for the other.
* Find the maximum depth reached by the tree that used the Gini impurity. Train multiple classifier by modifying the max_depth within the range from 1 to maximum depth and save the f1 scores to lists and print them.
* Compare the results from the train set with the results from the test set. What do you notice? Explain your findings. How are you going to choose the max_depth of your model?


# Data

The breast_cancer dataset is in sklearn library and you have to use  ***from sklearn.datasets import load_breast_cancer***


# Prerequisites

Basic sklearn functions for train-test split, metrics and DecisionTreeClassifier

# Exercise 2
This exercise is much more demanding than the first. You have to work with a dataset that includes both categorical and numerical attributes. There are also some missing values. So you have to build a pipeline from scratch.
* Load the income.csv file and train a DecisionTree model that will predict the income variable.
* Your pipeline should be able to handle missing values and categorical features. You can preprocess the dataset as you like in order to achieve higher scores
* Report the f1-score and accuracy score of the test set found in income_test.csv. 


# Data

You can load the train and test set from the data folder (income.csv and income_test.csv respectively)


# Prerequisites
Various modules from sklearn are demanding for this exercise to be completed. For example you can-must use: 
* sklearn.pipeline
* sklearn.tree import
* sklearn.metrics
* sklearn.model_selection
* sklearn.preprocessing
* sklearn.compose
* sklearn.preprocessing
* sklearn.impute