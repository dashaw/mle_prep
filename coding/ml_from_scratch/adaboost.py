#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:35:40 2022

@author: darrenshaw

recall
* boosting = growing multiple weak learners sequentially to overcome misclassifications
* approach
  * weak learner (in adaboost = decision stump, decision tree w/ one split)
  * combine weak learner in weighted sum approach to predict
  * either class [-1, +1]
  * error 
    * at time 0 = missclasification/num_samples
    * at time > 0 = sum of weights for all misclassifications
    * always between [0, 1]
  * weights
    * w_0 = 1/N for each sample
    * $w = (w*exp(-alpha * y * h(X))) / sum(w)
  * performance (alpha)
    * alpha = 0.5 * log((1-error)/error)
  * prediction = sign(sum(alpha*prediction)) for each weak learner
  
training
  * initialize weights for each sample = 1/N
  * choose number of weak learners and iterate
  * train each decision stump
  * claculate error of decision stump
  * calculate performance (alpha)
  * update weights
"""

import numpy as np

class DecisionStump:
    
    def __init__(self):
        self.polarity = 1
        self.feature_idx = None
        self.threshold = None
        self.alpha = None
        
    def predict(self, X):
        n_samples = X.shape[0]
        X_column = X[:,self.feature_idx]
        
        predictions = np.ones(n_samples)
        
        if self.polarity == 1:
            predictions[X_column < self.threshold] = -1
        else:
            predictions[X_column > self.threshold] = -1
            
        return predictions
    
class Adaboost:
    
    def __init__(self, n_clf=5):
        self.n_clf = n_clf
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        # init weights
        w = np.full(n_samples, (1/n_samples))
        
        self.clfs = []
        for _ in range(self.n_clf):
            clf = DecisionStump()
            
            min_error = float('inf')
            
            for feature_i in range(n_features):
                X_column = X[:, feature_i]
                thresholds = np.unique(X_column)
                for threshold in thresholds:
                    p = 1
                    predictions = np.ones(n_samples)
                    predictions[X_column < threshold] = -1
                    
                    missclassified = w[y != predictions]
                    error = np.sum(missclassified)
                    
                    if error > 0.5:
                        error = 1 - error
                        p = -1
                    
                    if error < min_error:
                        min_error = error
                        clf.polarity = p
                        clf.threshold = threshold
                        clf.feature_idx = feature_i
                        
            EPS = 1e-10
            clf.alpha = 0.5 * np.log((1-(error))/(error+EPS))
            
            predictions = clf.predict(X)
            
            w *= np.exp(-clf.alpha * y * predictions)
            # import pdb;pdb.set_trace()
            w = w/np.sum(w)
            
            self.clfs.append(clf)
            
    def predict(self, X):
        clf_preds = [clf.alpha * clf.predict(X) for clf in self.clfs]
        y_pred = np.sum(clf_preds, axis = 0)
        y_pred = np.sign(y_pred)
        return y_pred
        
    
    
    
    
    