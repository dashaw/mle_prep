#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:26:40 2022

@author: darrenshaw
"""

import numpy as np

class LinearRegression:
    
    def __init__(self, lr=1e-3, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        # init parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # iterative gradient descent
        for _ in range(self.n_iters):
            """
            in the original youtube videos, the author uses np.dot
            for the below operations, which doesn't really make sense because
            what is actually happening is matmul and numpy recommends
            us np.matmul in these scenarios.
            
            using np.dot will still implicitly perform matmul for 2-d arrays,
            but it is kind of confusing to read
            """
            y_hat = np.matmul(X, self.weights) + self.bias
            
            dw = (1/n_samples) * np.matmul(X.T, (y_hat - y))
            db = (1/n_samples) * np.sum(y_hat - y)
            
            self.weights -= self.lr*dw
            self.bias -= self.lr*db
    
    def predict(self, X):
        y_hat = np.dot(X, self.weights) + self.bias
        
        return y_hat