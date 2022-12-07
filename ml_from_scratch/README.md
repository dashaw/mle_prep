## Context
* Using [Machine Learning From Scratch In Python - Full Course With 12 Algorithms (5 HOURS)](https://www.youtube.com/watch?v=rLOyrWV8gmA) to prep for ML Coding rounds

## Notes
* Linear & Logistic Regression: recall these have the same updates (i.e., for any $w_{i}$ we compute $dw_{i}$ as the dot product between the feature vector of $x_{i}$ across all samples and the error vector $(y_{predicted} - y_{true})$
  * $w -= learning rate * dw$
  * in the videos the author does a great job! but keeps referring to np.dot() operations when what they are really doing is using np.matmul() (note: when a,b in np.dot(a,b) are 2-d arrays then it defaults to np.matmul()) which can be confusing and I've updated in my samples 
* Naive Bayes: recall that we treat feature as mutually independent, then when we look at Bayes theorem and simplify using logs it becomes
  * $y = argmax_{y} log(P(x_{1}|y)) + log(P(x_{2}|y) + ... + log(P(x_{n}|y)) + log(P(y))$
  * i.e., for each feature in sample, compute log of probability for that feature and class (using gaussian pdf and mean and variance of training data), add all these together and also add log of probability of class (aka prior)
* Preceptron: for each training sample x_{i}:
  * $w = w + \delta w$
  * $\delta w = learning\\_rate * (y_{i} - y_{predicted}) * x_{i}$
* SVM: recall that w is a unit vector from origin and perpendicular to hyperplane, b is offset from origin to decision boundary
  * if sample vector dot product with w is < b then classify negative, else classify positive
  * it can be shown taht if we minimize ||w|| then we maximize the distance of the decision boundary
  * it can be hard to remember, refer to [this guide](https://www.analyticsvidhya.com/blog/2021/10/support-vector-machinessvm-a-complete-guide-for-beginners/) if wanting to bursh up 
* Decision tree: recall that we grow tree/splits in a greedy fashion and have options on the mathematical approach for determining "best" split
  * one such approach is to use Entropy and Information Gain
  * $Entropy = - {\sum} p(X)*log_{2}(p(X))$ which is maximize when an even 50/50 split of each class
  * example: - (0.5*(-1) + 0.5*(-1)) = 1
  * to determine the Information Gain for a candidate split, $Information Gain = Entropy(parent) - ((weighted\\_average)*E(children))$
  * greedy search over all possible features and feature values
  * choose candidate split that maximizes IG
  * grow tree recursively until some condition
