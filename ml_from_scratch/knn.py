import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    #return np.sqrt(np.sum(x1-x2)**2)
    dist = np.sqrt(np.sum((x1 - x2)**2,axis=1))
    return dist

"""
class for k-nearest neighbors algo
"""

class KNN:
    
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        """
        predict for 1 or multiple samples
        """
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)
        
    def _predict(self, x):
        # compute distances
        """
        in the youtube series they use list comprehension to compute for each (x1,x2)
        pair which is kind of confusing when they could do this using matrix maths
        """
        distances = euclidean_distance(x,self.X_train)
        
        # get k-nearest neighbors & labels
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # return majority vote
        most_common = Counter(k_nearest_labels).most_common(1)
        
        return most_common[0][0]
    
