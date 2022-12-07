#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:42:55 2022

@author: darrenshaw
"""

import numpy as np
from decision_tree import DecisionTree
from collections import Counter
from time import time

def bootstrap_sample(X, y):
    n_samples = X.shape[0]
    idxs = np.random.choice(n_samples, size=n_samples, replace=True)
    return X[idxs], y[idxs]

class RandomForest:
    
    def __init__(self, n_trees=100, min_samples_split=2, max_depth=100, n_feats=None):
        self.n_trees = n_trees
        self.min_samples_split = min_samples_split 
        self.max_depth = max_depth 
        self.n_feats = n_feats
        self.trees = []
        
    def fit(self, X, y):
        for i in range(self.n_trees):
            t1 = time()
            print(f"growing tree # = {i+1}")
            tree = DecisionTree(min_samples_split=self.min_samples_split,
                                max_depth=self.max_depth,n_feats=self.n_feats)
            
            X_sample, y_sample = bootstrap_sample(X, y)
            tree.fit(X_sample, y_sample)
            print(f"time taken = {time()- t1}")
            
            self.trees.append(tree)
            
            
    def predict(self, X):
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        # tree_preds [[11111], [00000], [[11111]]]
        # output will be nested for a given tree
        # but we want to see for a given sample all preds for the forest,
        # so need to swap
        # need to convert structure
        tree_preds = np.swapaxes(tree_preds, 0, 1)
        
        # 101 001 101 000
        y_pred = [self._most_common_label(tree_pred) for tree_pred in tree_preds]
        return np.array(y_pred)
    
        
    def _most_common_label(self, y):
        counter = Counter(y)
        most_common = counter.most_common(1)
        
        return most_common[0][0]
        
