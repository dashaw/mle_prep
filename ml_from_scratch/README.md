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
  * $\delta w = (learningRate) * (y_{i} - y_{predicted}) * x_{i}$

* SVM: recall that w is a unit vector from origin and perpendicular to hyperplane, b is offset from origin to decision boundary
  * if sample vector dot product with w is < b then classify negative, else classify positive
  * it can be shown taht if we minimize ||w|| then we maximize the distance of the decision boundary
  * it can be hard to remember, refer to [this guide](https://www.analyticsvidhya.com/blog/2021/10/support-vector-machinessvm-a-complete-guide-for-beginners/) if wanting to bursh up 

* Decision Tree: recall that we grow tree/splits in a greedy fashion and have options on the mathematical approach for determining "best" split
  * one such approach is to use Entropy and Information Gain
  * $Entropy = - {\sum} p(X)*log_{2}(p(X))$ which is maximize when an even 50/50 split of each class
  * example: - (0.5*(-1) + 0.5*(-1)) = 1
  * to determine the Information Gain for a candidate split, $Information Gain = Entropy(parent) - ((weighted\\_average)*E(children))$
  * greedy search over all possible features and feature values
  * choose candidate split that maximizes IG
  * grow tree recursively until some condition
  * [REVISIT] this is a good example of recursive ML coding

* Random Forest: recall able to leverage base DecisionTree class to form multiple
  * bootstrap aggregating (aka, bagging):
    * 1. multiple subsets of data samples selected with replacement
    * 2. create model in parallel for each subset
    * 3. combine all predictions
    * 4. out-of-bag dataset = those not selected and can be used for eval on hold-out samples
  * reduces overfitting (high variance)

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

* Lineary independent comments:
  * linearly dependent vectors = there is some combination of vectors in the set that can be used to produce a subset of the vectors in the set
  * aka, it is adding nothing new in terms of info
  * span of vectors = vector space that can be represented by some combination of vectors in the set
  * PCA ensures that features of data are independent (i.e., we cannot combine some subset of features to equal and existing feature)

* K-Means
  * recall approach
    * randomly initialize cluster centers
    * until convergence
      * update labels (assign points to nearest center)
      * update cluster centers (set to mean of each center)

* Adaboost
  * recall
    * boosting = growing multiple weak learners sequentially to overcome misclassifications, weighing samples differently at each sequences
  * approach
    * weak learner (in adaboost = decision stump, decision tree w/ one split)
    * combine weak learner in weighted sum approach to predict
    * either class [-1, +1]
    * **error**
      * $\epsilon_{0} = \dfrac{misclassifications}{number samples}$
      * $\epsilon_{t} = \sum_{missclassified} weights$
      * choose stump that minimizes $\eta$
      * $\eta  between  [0, 1]$
    * **weights**
      * $\omega_{0} = \dfrac{1}{number samples}$
      * $\omega_{t} = \dfrac{\omega * y * h(X)}{sum(\omega)}$
      * for $h(X)$ = stump prediction
    * **performance (alpha)**
      * $\alpha = 0.5 * log((1-\epsilon)/\epsilon)$
  * **prediction**: $y = sign(\sum_{t} \alpha_{t} * h(X))$, aka across all weak learners
