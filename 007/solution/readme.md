## Solutions
### Model Name and File Name: (IBM_HR.ipynb)
1 svm.SVC
2 SGDClassifier
3 Perceptron
4 MultinomialNB
5 PassiveAggressiveClassifier
6 GaussianNB
7 GaussianProcessClassifier
8 KNeighborsClassifier
9 RandomForestClassifier
10 AdaBoostClassifier
11 ExtraTreesClassifier
12 GradientBoostingClassifier
13 MLPClassifier
14 QuadraticDiscriminantAnalysis
15 xgboost.XGBClassifier
16 cb.CatBoostClassifier
17 CNN

### Description:
Sturge’s rule:
Number of Bins = 1+log2(N) (Number of Samples)
In this case 10 bins means 10 folds

svm.SCV 85% and remaining algorithm above 90%

Grid Random Search from large values to closer to Best Parameters.

### Further details: 
Fold:KFold,GroupKFold,ShuffleSplit,RepeatedStratifiedKFold,StratifiedKFold,GroupShuffleSplit,StratifiedShuffleSplit,TimeSeriesSplit

### Model Accuracy (Classification Report):
- Confusion matrix
- F1 score
- precision
- recall  
- support