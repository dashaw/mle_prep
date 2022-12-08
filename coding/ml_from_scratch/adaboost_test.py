#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:16:24 2022

@author: darrenshaw
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from adaboost import Adaboost

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

data = datasets.load_breast_cancer()
X = data.data
y = data.target
y[y==0] = -1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)



ada = Adaboost(n_clf=5)
ada.fit(X_train,y_train)
predictions = ada.predict(X_test)

print(accuracy(y_test, predictions))