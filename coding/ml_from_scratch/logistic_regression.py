#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 08:16:19 2022

@author: darrenshaw
"""

import numpy as np

class LogisticRegression:
    
    def __init__(self, lr=1e-3, n_iters=1000, predict_thresh = 0.5):
        self.lr = lr
        self.n_iters = n_iters
        self.predict_thresh = predict_thresh
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        """

        Parameters
        ----------
        X : np.array of size mxn, training data
            DESCRIPTION.
        y : np.array of size mx1, labels

        Returns
        -------
        None.

        """
        
        # init parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iters):
            linear = np.matmul(X,self.weights) + self.bias 
            # (mxn)(nx1) --> (mx1)
            y_hat = self._sigmoid(linear)
            # mx1
            
            
            dw = (1/n_samples) * np.matmul(X.T, (y_hat-y))
            # X = mxn, mx1 --> (nxm) (mx1) --> (nx1)
             
            db = (1/n_samples) * np.sum(2*(y_hat-y))
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
    
    def predict(self, X):

        linear = np.matmul(X,self.weights) + self.bias 
        # (mxn)(nx1) --> (mx1)
        y_hat = self._sigmoid(linear)
        y_predicted = [1 if i >= self.predict_thresh else 0 for i in y_hat]
        return y_predicted
        
    
    def _sigmoid(self, linear):
        return 1/(1 + np.exp(-linear))