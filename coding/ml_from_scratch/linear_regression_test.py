#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:34:08 2022

@author: darrenshaw
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

X, y = datasets.make_regression(n_samples = 1000, n_features = 1, noise= 20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

print(X_train.shape)
print(y_train.shape)

from linear_regression import LinearRegression

regressor = LinearRegression(lr=0.01, n_iters=500)
regressor.fit(X_train, y_train)
pred = regressor.predict(X_test)

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)
    
mse_value = mse(pred,y_test)
print(mse_value)


fig = plt.figure(figsize=(10,6))
plt.scatter(X[:,0], y, color = "b", marker = "o", s = 30)
plt.scatter(X_test, pred, cmap=(0.5), s=10)
plt.show()
