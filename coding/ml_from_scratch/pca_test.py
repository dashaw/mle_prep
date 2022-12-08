#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 11:23:09 2022

@author: darrenshaw
"""

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from pca import PCA

data = datasets.load_iris()
X = data.data
y = data.target

pca = PCA(2)
pca.fit(X)
X_projected = pca.transform(X)

x1 = X_projected[:,0]
x2 = X_projected[:,1]

plt.scatter(x1,x2)