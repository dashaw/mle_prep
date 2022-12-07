#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:40:22 2022

@author: darrenshaw
"""

import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from kmeans import KMeans

X, y = make_blobs(centers=4, n_samples=500, n_features=2, shuffle=True, random_state=42)

clusters = len(np.unique(y))

k = KMeans(clusters)
y_pred = k.predict(X)

k.plot()