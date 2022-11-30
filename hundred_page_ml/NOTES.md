## [Book pdf](http://ema.cri-info.cm/wp-content/uploads/2019/07/2019BurkovTheHundred-pageMachineLearning.pdf)

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
