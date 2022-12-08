#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:13:37 2022

@author: darrenshaw

linear model w*x -b = 0

y_i(w*x_i - b) >= 1


"""

import numpy as np

class SVM:
    
    def __init__(self, lr=0.001,lambda_param = 0.01,n_iters = 1000):
        self.lr = lr
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None
        
    def fit(self, X, y):
        y_ = np.where(y <= 0, -1, 1)
        n_samples, n_features = X.shape # mxn, m samples, n features
        
        # init params
        self.w = np.zeros(n_features)
        self.b = 0
        
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i,self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2*self.lambda_param*self.w)
                else:
                    self.w -= self.lr * (2*self.lambda_param*self.w) - np.dot(x_i,y_[idx])
                    self.b -= y_[idx]
        
    def predict(self, X):
        linear_output = np.matmul(X,self.w) - self.b
        return np.sign(linear_output)