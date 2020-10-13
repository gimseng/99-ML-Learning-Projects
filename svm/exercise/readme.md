# Problem Statement

The aim of the exercise is to implement Support Vector Machine (SVM) from scratch.
The basic implementation is done for understanding.

# Objective

To understand how SVM works internally and fine-tune hyperparameters of SVM.

# Task

- Implementing an SVM class that defines methods for learning and predicting from data.
- Understanding and implementing the concept of linear kernel in SVM
- Extracting features from the spam/ham dataset
- Using the SVM algorithm for classification of spam and ham in spam dataset regression using appropriate dataset.
-  Visit [this](https://www.kaggle.com/uciml/sms-spam-collection-dataset) site for dataset.

# SVM Algorithm

Support Vector machine (SVM) algorithm is a type of supervised ML algorithm which can be used for both classification as well as regression predictive problems. The objective of SVM is to find a hyperplane in an n-dimensional space (n- number of features) that can classify a set of data points.
The following objective would define SVM:
-  finding a hyperplane that has the maximum margin- the maximum distance between data points of both classes (positive and negative classes).

The following concepts are required for understanding the SVM algorithm for linear kernel.

1. Linear kernel is defined by the following equation: xi.w + b where xi is the training sample, w is the weight and b is the bias.

2. For all xi in the training data, the following condition is applied when using linear SVM:

* ```	
		 	xi.w + b <= -1   if yi = -1 (belongs to -ve class)
		 	xi.w + b >= +1	if yi = +1 (belongs to +ve class)
		 				or
		 	 	__yi(xi.w+b) >= 1__
		 	```


3. For all support vectors(SV) (data points which decides margin)
* ```
			xi.w+b = -1    here xi is -ve SV and yi is -1
			xi.w+b = +1    here xi is +ve SV and yi is +1
			```
* For decision Boundary `yi(xi.w+b)=0` here xi belongs to point in decision boundary
* Our Objective is to maximize Width W
		* `W = ((X+ - X-).w)/|w|`
		* or we can say minimize |w|
* Once we have found optimized w and b using algorithm
		* `x.w+b = 1` is line passing through +ve support vectors
		* `x.w+b = -1` is line passing through -ve support vectors
		* `x.w+b = 0` is decision boundary
* It is not necessary that support vector lines always pass through support vectors
* It is a Convex Optimization problem and will always lead to a global minimum
* This is Linear SVM means kernel is linear             

The algorithm should be implemented as follows:
1. Load the data
2. Extract the features from the spam/ham dataset
3. Implement the SVM class and fit and predict functions
4. In the SVM class, define and initialize the lambada parameter, learning rate, weights and biases. In this case the lamabda parameter and learning rate are regularization parameters for SVM, and weights are being trained using the linear SVM kernel
5. In the predict function, a linear kernel is defined by xi.w+b . Return the result of xi.w+b along with the sign in this function.
6. In the fit function, check for the sign of y, the actual value of target variable. If y is less than or equal to 0, set equal to -1. If y is greater than 0, set y to 1. Get the number of training samples and number of features using the shape of input matrix X. Set the weights equal to a numpy array of zeros equal to the size of number of features. In this function, we will be training the linear svm model for a specific number of iterations. Hence, here for each epoch while training the model, we will take a traning sample xi and calculate the objective function:  yi(x.w)+b>=1. If the objective function calculated is greater than or equal to one, update the weights. If the objective function is less than 1, update the weights and bias  



Here is a template notebook to get you started:

`svm_starter_exercise.ipynb`

[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gimseng/99-ML-Learning-Projects/blob/master/svm/exercise/svm_starter_exercise.ipynb)
[![View in nbviewer](https://github.com/jupyter/design/blob/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/gimseng/99-ML-Learning-Projects/blob/master/svm/exercise/svm_starter_exercise.ipynb)

### References
- https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47
