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

## Chapter 4: Anatomy of a learning algorithm

Three basic parts
* a loss function
* an optimization criterion based on the loss function (e.g., cost function)
* an optimization routine leveraging training data to find solution to optimization criterion

Gradient descent
* used to find optimal parameters for linear and logistic regression, SVM, neural networks, etc.
* many models, such as logistic regression or SVM, the optimization criterion is convex
* convex functions have only one minimum, which is global. Optimization criteria for neural networks are not convex, but inpractice even finding a local minimum suffices

<img src="images/gradient_descent_basic.png" alt="drawing" width="700"/>

* The gradient descent algorithm is sensitive to the choice of the step –. It is also slow for large datasets. Fortunately, several significant improvements to this algorithm have been proposed. Stochastic gradient descent (SGD) is a version of the algorithm that speeds up the computation by approximating the gradient using smaller batches (subsets) of the training data. SGD itself has various “upgrades”. Adagrad is a version of SGD that scales – for each parameter according to the history of gradients.As a result, – is reduced for very large gradients and vice-versa. Momentum is a method that helps accelerate SGD by orientingthe gradient descent in the relevant direction and reducing oscillations. In neural network training, variants of SGD such as RMSprop and Adam, are most frequently used.

## Chapter 5: basic practice

* Standardization vs. normalization
  * in practice for unsupervised standardization > normalization
  * also preferred for a feature that can have extreme outliers as it will "squeeze" the normal values into small range
  * most other cases, noramlization is preferred

* Data imputation
  * obviously can replace with average, median, etc.
  * more advanced approach is to treat missing feature value as a regression problem

* Three sets
  * training set = biggest, build model
  * validation set = roughly same size as test, use to choose learning algo and hyperparams
  * test set = true gauge of model performance

<img src="images/algo_cheat_sheet.png" alt="drawing" width="700"/>

* Regularization
  * l1 = lasso, sparse, feature selection
  * l2 = ridge
  * also elastic net which is combo ofboth

* Evaluation
  * preicsion = TP / (TP + FP)
  * recall = TP / (TP + FN)
  * if wanting to do these for multi-class, pick a class you care about, set to 1 and treat all other classes as 0
  * accuracy = (TP + TN) / (TP + TN + FP + FN)
  * area under roc curve:
    * TPR = TP / (TP + FN)
    * FPR = FP / (FP + TN)
* Tuning
  * easy approach is grid search on hyperparams
  * train on train set, select params based on validation, understand performance on test

* Cross-validation
  * when you don't have decent validation set to tune hyperparams, common to us cross-validation
  * e.g., 5 fold CV

## Chapter 6: Neural networks

* Activation fn
  * Differentiable for gradient descent
  * Nonlinear component = allow neural network to approximate nonlinear functions
  * Without nonlinearities, _f_neural_network would be linear no matter how many layers
  * I.e., linear function of a linear function = linear

<img src="diagrams/nn_activation_fn.png" alt="drawing" width="700"/>

* Historic problems
  * exploding gradients: easier to deal with using easy techniques like gradient clipping, l1/l2 regularization
  * vanishing gradients: traditionally more difficult to deal with

* Vanishing radient
  * in some cases, gradient will be vanishingly small = effectively preventing some parameters from changing their value
  * worse case = completely stop NN from further training

* Traditional activation functions
  * E.g., hyperbolic tangent has gradients in range (0,1) and so backpropogation computes by chain rule
  * Effect = multiplying n of these small numbers to compute gradients of the earlier (leftmost) layers in a _n_-layer network means that gradient decreases expoentially with _n_
  * Result is that the effect that the earlier layers train very slow, if at all

* Modern techniques
  * Modern implementations allow to train very deep architectures
  * This includes ReLU, LSTM (and other gated united), skip connections, + other advanced modifictions of gradient descent algo
  * In practice, many business problems can be solved with NN having 2-3 layers b/w the input and output

* Growing size
  * as you add layers, you add (size_l-1 + 1)*size_l parameters
  * E.g., if you add another 1000-unit layer to an existing network, then you add more than 1 million additional parameters to your model

* Convolutional neural network
  * significantly reduces number of parameters in DNN
  * mostly used in imag eand text
  * <see book for depictions on how convultional filters are used>

* Recurrent neural network (RNN)
  * used to label, classify, generate sequences
  * sequence = a matrix, each row of which is a feature vector and the order of rows matters
  * not feed-forward: contains loops
  * each unit _u_ of a recurrent layer _l_ has a real-valued **state** h_l,u
  * state can be seen as the memory of the unit
  * in RNN, each unit _u_ in each layer _l_ receives two inputs: a vector of states from the previous layer _l_ - 1 and the vector of states from this same layer _l_ from the previous time state
  * backpropagation through time = from pov of gradient calculation, longer the input sequence, the deeper is the unfolded network
  * as length of the input sequence grows, the feature vectors from the beginning of the sequence tend to be "forgotten" because the state of each unit, which serves as the network's memory, becomes significantly affected by the feature vectors read more recently
  * most effective are **gated RNNs**, which includes **long short-term memory (LSTM)** and networks based on the **gated recurrent unit (GRU)**
