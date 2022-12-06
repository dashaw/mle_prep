## Context
* Using [Machine Learning From Scratch In Python - Full Course With 12 Algorithms (5 HOURS)](https://www.youtube.com/watch?v=rLOyrWV8gmA) to prep for ML Coding rounds

## Notes
* linear/logistic regression: recall these have the same updates (i.e., for any $w_{i}$ we compute $dw_{i}$ as the dot product between the feature vector of $x_{i}$ across all samples and the error vector $(y_{predicted} - y_{true})$
  * $w -= learning rate * dw$
  * in the videos the author does a great job! but keeps referring to np.dot() operations when what they are really doing is using np.matmul() (note: when a,b in np.dot(a,b) are 2-d arrays then it defaults to np.matmul()) which can be confusing and I've updated in my samples 
* naive bayes: recall that we treat feature as mutually independent, then when we look at Bayes theorem and simplify using logs it becomes
  * $y = argmax_{y} log(P(x_{1}|y)) + log(P(x_{2}|y) + ... + log(P(x_{n}|y)) + log(P(y))$
  * i.e., for each feature in sample, compute log of probability for that feature and class (using gaussian pdf and mean and variance of training data), add all these together and also add log of probability of class (aka prior)
 
