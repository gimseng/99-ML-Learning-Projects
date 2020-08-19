# Problem Statement

The data description is provided in [./data/readme.md](https://github.com/gimseng/99-ML-Learning-Projects/blob/master/006/data/readme.md). This is a classification of tumorous data task. Classify each patient's tumor as either malignant or benign. 
The aim of this exercise is to learn how to create ensemble techniques and compare them. 
A summary of each technique is provided at the end of this readme.


# Exercise goals

- Read the data and create train-test sets. 
- Perform preprocessing and normalize the data
- Implement Bagging (Random Forest), AdaBoost, Gradient Boosting and XGBoost with standard settings as provided by the libraries. 
- Iterate through a pre-defined set of parameters and select the best configuration. 


# Summary of techniques/methods

## Bagging
Bagging is the process of creating sub-divisions of the dataset randomly and apply basis functions on them. The final result is obtained by aggregating the individual results. Both decision trees and random forests are easy basis functions as visual comprehension of dividing the data is feasible. 

Pros:

* Prevents overfitting and decreases varience
* Easy to set up
* Better results than any consitituent predictor

Cons:

* Doesn't reduce varience
* Computationally complex
* Voting and averaging results is not a good practice

Hint: First create a classifier, say decision tree. Create a Balanced Bagging Classifier from imblearn.ensemble and pass the DT/RF to the bagging basis function. 

## Boosting
Boosting is a general ensemble technique which refocuses on the poorly functioning basis function by keeping track of the net error on each trainers' each epoch. 

Pros:

* Makes weak learners stronger (at least theoretically)
* Removes bias and prevents underfitting

Cons:

* Computationally expensive
* Susceptible to overfitting 

### AdaBoost
AdaBoost is a meta-heuristic responsible for taking multiple weak basis functions and aggregating them into a overall strong classifier. In this solution n_estimators specify the number of models being trained. The overall measure-of-goodness is a measure of minimizing the exponential loss function. It provides a high degree of precision and cascades weak learners optimally. However, the loss function is set. 

Hint: Follow the same process as bagging, with the replacement of bagging classifier with adaboost. Don't worry about the accuracy levels for now. 

### Gradient boosting
This is a generalized form of AdaBoost which provides a set of loss function to chose from. The expanded choice of loss function provides a sort of feedback which makes every subsequent classifier spwaned better than it's predecessor. 

### XGBoost
It is similar to GradientBoosting, with the inclusion of Lasso and Ridge regularization techniques. This curbs any overfitting in GB. It offers parallelization,  distributed computing, cache optimization, and out-of-core computing.


## Stacking
Stacking is an ensemble technique which aims to combine multiple base learners iteratively to create an optimal combination. Multiple base learners are trained on sets of training data and then tested on a held-out testing set. The main aim is to find the perfect combination. The only drawback would be the division of data really thins out the total amount of data. 

## Ploting decision boundaries
As an added exercise try plotting the decision boundary for a classifier. The decision boundary for this particular dataset might not be very encouraging, but don't lose heart. As a tutorial, the standard data set of make_moons from sklearn.datasets has been plotted for AdaBoost in the solutions sections. Try doing it for the other classifiers. 

