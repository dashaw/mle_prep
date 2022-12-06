#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:15:05 2022

@author: darrenshaw
"""

import numpy as np

class NaiveBayes:
    
    def __init__(self):
        pass
    
    def fit(self, X, y):
        # X is numpy.ndarray
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)
        
        # init mean, variance, prior
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors = np.zeros(n_classes, dtype=np.float64)
        
        # calculate
        for c in self._classes:
            X_c = X[c==y]
            self._mean[c,:] = X_c.mean(axis=0)
            self._var[c,:] = X_c.var(axis=0)
            self._priors[c] = X_c.shape[0]/float(n_samples)
    
    def predict(self, X):
        # i.e., we are using list comprehension for prediction on each sample
        # is there a vectorized way of doing this same thing?
        y_pred = [self._predict(x) for x in X]
        return y_pred
        
    
    def _predict(self, x):
        posteriors = []
        
        for idx, c in enumerate(self._classes):
            prior = np.log(self._priors[idx])
            
            class_conditional = np.sum(np.log(self._pdf_normal(idx, x)))
            
            posterior = class_conditional+prior
            posteriors.append(posterior)
            
        return self._classes[np.argmax(posteriors)]
    
    
    def _pdf_normal(self, class_idx, x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(- (x-mean)**2 / (2*var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator
        