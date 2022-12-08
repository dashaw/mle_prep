#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:06:44 2022

@author: darrenshaw
"""

import numpy as np

class Perceptron:
    
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = 0
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        # m x n
        
        # init weights
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        y_ = np.array([1 if i > 0 else 0 for i in y])
    
        # learn/update params
        for _ in range(self.n_iters):
            for ind, x_i in enumerate(X):
                linear_output = np.dot(x_i,self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                update = self.lr * (y_[ind] - y_predicted)
                self.weights += update * x_i
                self.bias += update
                
    
    def predict(self, X):
        linear = np.matmul(X,self.weights) + self.bias
        y_predicted = self.activation_func(linear)
        return y_predicted
    
    def _unit_step_func(self, x):
        return np.where(x>=0, 1, 0)