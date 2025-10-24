# Support Vector Machine (SVM) Exercise

**Objective:**  
Learn how Support Vector Machines (SVMs) classify data by finding the best separating boundary (hyperplane) between classes.

---

## Step 1: Introduction

Support Vector Machines are supervised learning models used for classification and regression tasks.  
They work by finding the hyperplane that best separates different classes in a dataset.  
SVMs can handle both **linear** and **non-linear** data using kernel functions.

---

## Step 2: Dataset Preparation

Let’s use the famous **Iris dataset** from scikit-learn to visualize how SVMs work.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

```

## Step 3: Train an SVM Model

```python
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Create SVM classifier
model = SVC(kernel='linear', C=1)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
```

## Step 4: Visualize the Decision Boundary

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_decision_boundary(X, y, model):
    X = X[:, :2]  # use only two features for easy visualization
    h = .02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
    plt.title("SVM Decision Boundary (Linear Kernel)")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

plot_decision_boundary(X_train, y_train, model)
```

## Step 5: Try Different Kernels

```python
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

kernels = ['linear', 'poly', 'rbf', 'sigmoid']

for kernel in kernels:
    model = SVC(kernel=kernel, C=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\nKernel: {kernel}")
    print("Accuracy:", accuracy_score(y_test, y_pred))
```


## Step 6: Summary

In this exercise, you learned how to:

- Load and preprocess data (Step 2)
- Train an SVM classifier (Step 3)
- Visualize decision boundaries (Step 4)
- Experiment with different kernels (Step 5)

This helps understand how SVMs find the optimal boundary between classes — a key concept in machine learning.


**Tags:** #MachineLearning #SVM #Python #Hacktoberfest #BeginnerFriendly

