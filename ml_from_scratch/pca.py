#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:22:56 2022

@author: darrenshaw


* PCA
  * recall motivation:
    * linearly independent features
    * dimensionality reduction
    * find a transformation such that transformed features are linearly independent
    * dimensionality can be reduced by using dimensions with highest importances
    * should have maximum variance
  * $VAR(X) = (1/n) \sum (X_{i} - X_{mean})^2$
  * $Cov(X, Y) = (1/n) \sum (X_{i} - X_{mean})(Y_{i} - Y{mean})^T$
  * $Cov(X, X) = (1/n) \sum (X_{i} - X_{mean})(X_{i} - X{mean})^T$
  * Reduces to eigenvector/eigenvalue problem
    * eigenvectors point in maximum variance
    * corresponding eigenvalue indicate importance
    * $Av = \lambda v$
  * Approach
    * substract mean from X
    * calculate cov(X,X)
    * calculate eigenvectors/values of covariance matrix
    * sort eigenvectors descending
    * choose k eigenvectors as the new k dimensions
    * transform original n dimensional data into k dimensions (aka with dot product)
  * new data will be linearly independent as dimensions are orthogonal
"""

import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None
        
    def fit(self, X):
        # mean
        self.mean = np.mean(X, axis=0)
        X = X - self.mean
        
        # calculate covariance
        cov = np.cov(X.T) # need to trnasform b/c function assume column vectors
        
        # eigenvectors/values
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        # 1 column will be an eigenvector
        eigenvectors = eigenvectors.T
        
        # sort eigenvectors
        idxs = np.argsort(eigenvalues)[::-1]
        # because originally in ascending order
        
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]
        
        self.components = eigenvectors[0:self.n_components]
        
    
    def transform(self, X):
        # transform data
        X = X - self.mean
        X_tfrm = np.matmul(X,self.components.T)
        # X = mxn, components = nxk
        # want mxk
        
        return X_tfrm
        
    
        