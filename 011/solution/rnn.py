# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 17:55:18 2021

@author: prads
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset_train = pd.read_csv("Google_Stock_Price_Train.csv")
train_set = dataset_train.iloc[:,1:2].values

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
scaled_training = sc.fit_transform(train_set)

x_train = []
y_train = []

for i in range(60,1258):
    x_train.append(scaled_training[i-60:i,0])
    y_train.append(scaled_training[i,0])
    
"""iteration 1 :
    x_train.append(scaled_training[0:60,0])
    y_train.append(scaled_training[60,0])
    x_tarin = [0,1,2,3,4,5,6,7,8,9,10  ..... 59]
    y_train =  [60]
iteration 2 :
    x_train.append(scaled_training[1:61,0])
    y_train.append(scaled_training[61,0])
    x_tarin = [[0,1,2,3,4,5,6,7,8,9,10  ..... 59],
               [1,2,3,4,5,6,7,8,9,10,11 .......60]]
    y_train =  [[60],[61]]    
iteration 3 :
    x_train.append(scaled_training[2:62,0])
    y_train.append(scaled_training[62,0])
    x_tarin = [[0,1,2,3,4,5,6,7,8,9,10  ..... 59],
               [1,2,3,4,5,6,7,8,9,10,11 .......60],
               [2,3,4,5,6,7,8,9,10,11 .......61]]
    y_train =  [[60],[61],[62]]
iteration 1258 """

x_train,y_train = np.array(x_train),np.array(y_train)

x_train.shape
y_train.shape

print(x_train.ndim, y_train.ndim)




x_train = np.reshape(x_train,(1198,60,1))

x_train.shape

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense ,LSTM,Dropout
model = Sequential()
model.add(LSTM( units = 60 ,return_sequences = True , input_shape = (60,1)))
model.add(Dropout(0.2))
model.add(LSTM( units = 60 ,return_sequences = True))
model.add(Dropout(0.2))
model.add(LSTM(units = 60 , return_sequences = True))
model.add(Dropout(0.2))
model.add(LSTM(units = 60 ))
model.add(Dropout(0.2))

model.add(Dense(units =1))
model.compile("rmsprop",loss = "mean_squared_error")
model.fit(x_train,y_train,epochs = 300)

dataset_test = pd.read_csv("Google_Stock_Price_Test.csv")
y_test = dataset_test.iloc[:,1:2]

dataset_total = pd.concat((dataset_train["Open"],dataset_test["Open"]),axis = 0)
inputs  = dataset_total[len(dataset_total)-len(dataset_test)- 60:].values
inputs = inputs.reshape(-1,1)

inputs = sc.fit_transform(inputs)

x_test = []
for i in range(60,80):
    x_test.append(inputs[i-60:i,0])
x_test = np.array(x_test)
x_test= np.reshape(x_test,(20,60,1))

ypred = model.predict(x_test)
ypred.shape
ypred = sc.inverse_transform(ypred)

plt.plot(y_test, color ="red", label = "actual stock price")
plt.plot(ypred, color ="blue",label = "predicted stock price")
plt.show()

test= []
for i in range (60 ,120): 
  test.append(i)
test = np.array(test) 
test = test.reshape(-1,1)
test = np.reshape(test, (1,60,1))
yp = model.predict (test)

yp = sc.inverse_transform(yp)
print(yp)
test =  [343,456,756,678,786,456,567,343,767,123,343,456,756,678,786,456,567,343,767,123,343,456,756,678,786,456,567,343,767,123,343,456,756,678,786,456,567,343,767,123,343,456,756,678,786,456,567,343,767,123,343,456,756,678,786,456,567,343,767,123]
len(p)
test = np.array(test) 
test = test.reshape(-1,1)
test = np.reshape(test, (1,60,1))
yp = model.predict (test)
yp = sc.inverse_transform(yp)
print(yp)










