#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:12:45 2022

@author: darrenshaw

recall: 
* entropy = $- {\sum} p(X)*log_{2}(p(X))
* information gain = E(parent) - (weighted average)*E(children)
* choose split which maximizes information gain
* greedy search = over all possible features and feature values
"""

import numpy as np
from collections import Counter

def entropy(y):
    # helper function (global) to compute entropy using above eqn
    hist = np.bincount(y)
    px = hist/len(y)
    entropy = -1*np.sum([p*np.log2(p) for p in px if p > 0])
    
    return entropy

class Node:
    
    def __init__(self, feature=None, threshold=None, left=None, right=None,*,value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf_node(self):
        # figure out if this is a leaf node
        return self.value is not None
    
class DecisionTree:
    
    def __init__(self, min_samples_split=2, max_depth=100, n_feats=None):
        self.min_samples_split = min_samples_split 
        self.max_depth = max_depth 
        self.n_feats = n_feats 
        self.root = None
        
    def fit(self, X, y):
        # grow our tree
        
        # random feature piece, how many features to consider?
        self.n_feats = X.shape[1] if not self.n_feats else min(self.n_feats, X.shape[1])
        
        # grow tree
        self.root = self._grow_tree(X, y)
        
    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))
        
        # --------
        # check for stopping criteria
        # --------
        if (depth >= self.max_depth or n_labels == 1 or n_samples < self.min_samples_split):
            
            leaf_value = self._most_common_label(y)
            
            return Node(value=leaf_value)
        
        
        # --------
        # continue
        # --------
    
        # choose random features
        feat_idxs = np.random.choice(n_features, self.n_feats, replace=False)
        
        # greedy search
        best_feat, best_thresh = self._best_criteria(X, y, feat_idxs)
        left_idxs, right_idxs = self._split(X[:, best_feat], best_thresh)
        left = self._grow_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right = self._grow_tree(X[right_idxs, :], y[right_idxs], depth+1)
        return Node(best_feat, best_thresh, left, right)
    
    def _best_criteria(self, X, y, feat_idxs):
        best_gain = -1
        
        split_idx, split_thresh = None, None
        
        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)
            
            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)
                
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold
                    
        return split_idx, split_thresh
    
    
    def _information_gain(self, y, X_column, split_thresh):
        # calculate parent entropy
        parent_entropy = entropy(y)
        
        # generate split
        left_idxs, right_idxs = self._split(X_column, split_thresh)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0
        
        # weighted average of child entropies
        n = len(y)
        n_left = len(left_idxs)
        n_right = len(right_idxs)
        e_l, e_r = entropy(y[left_idxs]), entropy(y[right_idxs])
        child_entropy = (n_left/n)*e_l + (n_right/n)*e_r
        
        
        # return information gain
        ig = parent_entropy - child_entropy
        return ig
        
        
    def _split(self, X_column, split_thresh):
        left_idx = np.argwhere(X_column <= split_thresh).flatten() # only want 1-d vector
        right_idx = np.argwhere(X_column > split_thresh).flatten()
        
        return left_idx, right_idx
        
        
    def _most_common_label(self, y):
        counter = Counter(y)
        most_common = counter.most_common(1)
        
        return most_common[0][0]
        
        
    def predict(self, X):
        # predict class, traverse tree
        return np.array([self._traverse_tree(x, self.root) for x in X])
    
    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)
    
    
    
    
    
    
    
    
    
    
    
    
    