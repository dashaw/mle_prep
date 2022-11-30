## [Book pdf](http://ema.cri-info.cm/wp-content/uploads/2019/07/2019BurkovTheHundred-pageMachineLearning.pdf)
## [Other github link](https://github.com/Chrisackerman1/The-Hundred-Page-Machine-Learning-Book)

## Chapter 1

Easy dicussion of different learning types.

#### Supervised learning
At this point, you should retain the following: any classification learning algorithm that
builds a model implicitly or explicitly creates a decision boundary. The decision boundary
can be straight, or curved, or it can have a complex form, or it can be a superposition of
some geometrical figures.

In practice, there are two other essential dierentiators of learning algorithms to consider:
speed of model building and prediction processing time. In many practical cases, you would
prefer a learning algorithm that builds a less accurate model fast. Additionally, you might
prefer a less accurate model that is much quicker at making predictions.

## Chapter 2

Extremely helpful, accessible reminder of math concepts: notation, derivation, chain rule, random variables, mean, std deviation, interals

Unbiased estimator = often we do not know _f_(x), but have samples. 

Parameter vs. instance-based models: parameter = has parameters, instance = used all samples (e.g., kNN)

## Chapter 3: Fundamental Algorithms

* No continuous derivative = function not smooth. Functions that are not smooth create unnecessary diculties when employing linear algebra to find closed form solutions to optimization problems. Closed form solutions to finding an optimum of a function are simple algebraic expressions and are often preferable to using complex numerical optimization methods, such as gradient descent (used, among others, to train neural networks).

* Finally, why do we care about the derivative of the average loss? Remember from algebra that if we can calculate the gradien of the function in eq. 2, we can then set this gradient to zero2 and find the solution to a system of equations that gives us the optimal values **w** and **b**. 

### Logisitc regression
* Leverage simoid function = 1/(1+e^-x) to keep output values [0, 1]
* So our model = 1/(1+e^-(wx+b))
* In linear regression we minimized MSE. In logistic instead of using squared loss we maximize the likelihood of training set according to the model. I.e., in stats likliehood function defines how likely the observations are according to our model.
* Optimization criterion = **maximum likliehood**: 

L = Product( f(x)^y * (1-f(x))^(1-y) )
--> maximize log(liklihood) = Sum( y*ln(f(x)) + (1-y)*ln(1-f(x))

Contrary to linear regression, there's no closed form solution to the above optimization problem. Typically numerical optimization procedure used in such cases is gradient descent.

### Decision trees
* Non-parametric model
* Focus on ID3 learning algo
  1. search through all features j= 1,..,_D_ and at all thresholds _t_, and split the set _S_ into two subsets
  2. evaluate potential split
  3. choose best split

#### Goodness of split
* For ID3, estimated using entropy
* Entropy = measure of uncertainty about a random variable
* Reaches maximum when all values of the RV are equiprobable
* Reaches minimum when value of random variable can only have one value
* Entropy = H(S) = -_f_*ln(_f_) - (1 - _f_)*ln(1-_f_)
* Entropy for a given feature and threhsold is weighted sum of the two entropies
* H(S-,S+) = |S-|/|S|*H(S-) + |S+|/|S|*H(S+)

### Support Vector Machine
* To extend SVM to cases with data no linearly seperable we introduce the hinge loss function = max(0, 1-y(wx-b))
* Hinge = 0 for data on correct side of decision boundary
* For data on wrong side, function's value is proportional to distance from decision boundary
* Goal is then to minimize following cost function:

`C||w||^2 + 1/N SUM( max(0, 1-y(wx-b))`

* Hyperparam C determines tradeoff between increasing size of decision boundary and ensuring x lies on correct side
* SVMs that optimize hinge loss = soft-margin SVMs
* C regulates tradeoff b/w classifiying training data well vs. generalizing

#### Dealing with non-linearity
* Goal = transform original space into space of higher dimensionality, which we hope is then linearly separable
* In SVM, use a function to implicitly transform original space into higher dimension during the cost function optimization = **kernel trick**
* But finding explicit mapping is hard
* Instead, use kernel functions to efficiently work in higher-dimensional space without doing so explicitly

* Traditional method to solve optimization problem in SVM is method of Lagrane multipliers
* Instead of solving original problem, formulate as <see pdf>
* Essentially we find out we are only interested in the dot-product between feature vectors
* Most widely used kernel is RBF (radial basis function)

`k(x, x') = exp(- ||x - x'||^2 / 2sigma^2)`

where ||x - x'||^2 = squared euclidean distance between two feature vectors

### k-Nearest Neighbors
* Non-parametric learning algorithm
* Keep all training examples in memory
* Once new unseen example comes, find k training examples closest, return majority label

* **Closeness** defined by distance function. Could be euclidean, cosine, etc.
* Cosine similarity = x.y / |x|*|y|

