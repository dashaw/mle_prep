#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:27:50 2022

@author: darrenshaw
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from perceptron import Perceptron

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

X, y = datasets.make_blobs(n_samples = 150, n_features = 2, centers = 2, cluster_std=1.05)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

p = Perceptron()
p.fit(X_train, y_train)
predictions = p.predict(X_test)

print(accuracy(y_test, predictions))

