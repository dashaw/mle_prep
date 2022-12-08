## Notes from various [StatQuest](https://www.youtube.com/@statquest) vids

### [Odds & probability](https://www.youtube.com/watch?v=ARfXDSkQf1Y&t=0s)
* $odds = \dfrac{p}{1-p}$
* odds = ratio of something happening to it not happening
* odds in [0, inf]
  * for p <= 0.5 --> odds in [0, 1]
  * for p > 0.5 --> odds in [1, inf]
* this is a significant asymetry which makes comparison difficult
* taking log(odds) solves this by making everything symetric
* e.g.,
  * if odds are 1 to 6 --> lodds = 0.17, log(odds) = -1.79
  * if 6 to 1 --> odds = 6, log(odds) = 1.79
* using log function, distance to origin is same for 1 to 6 as well as 6 to 1 odds
* log of ratio of probabilities = logit function = basis for logistic regression
* probability in [0,1] and ratio of (# success / # total attempts)

### [Logistic Regression series](https://www.youtube.com/watch?v=vN5cNN2-HWE)
* cannot use least-squares like linear regression, so instead use maximum likelihood (i.e., update params to maximize this likelihood)
* our target is in [0, 1], but in linear regression y-axis is [-inf, inf], to solve this problem the y-axis in logistic is transformed from probability to log(odds) meaning it can also go [-inf, inf]
* where $log(odds) = log\dfrac{p}{1-p}$
* coefficients are presented in terms of the log-odds graph
* **fitting a line**
  * when in log-odds space, we push negative and positive labels to -inf, +inf
  * therefore we cannot use residuals (least squares) because residuals will also be -inf and +inf 
  * solution = use maximum likelihood
  * approach:
    1. project original data points onto candidate line, so each sample will then have a candidate log(odds) value
    2. then transform candidate log(odds) to probabilities via $p = \dfrac{exp(log(odds))}{1+exp(log(odds))}
    3. now we are in probability space, compute the likelihood for each class: for each point, see it's probability (y-axis value)
    4. for class 1 samples: take product of all y-axis probabilities (e.g., might be 0.49x0.9x0.91x0.92
    5. do the same for class 0: take product of all y-axis 1-probabilities (e.g., might be 0.1x0.2x)
    6. technically we usually do log(likelihood for compute math/compute purposes but either works)
    7. so, log(likelihood) = log(0.49) + log(0.9) + log(0.91) + ... + log(0.2) = -3.77
    8. now update params and for new fit, compute log(likelihood)
    9. keep rotating log(odds) line to find what maximizes the log(likelihood)

* **derivation**
  * assume log-odds of an observation can be expressed as a linear model
    * $log \dfrac{P(x)}{1-P(x)} = \sum_{j=0} b_{j}x_{j}$
    * from this we can solve for $P(x)$ explicitly as $P(x) = \dfrac{exp(z)}{1+exp(z)}$ for $z = \sum_{j=0} b_{j}x_{j}$
    * our goal is then to find a fit (and therefore params) that maximizes the liklelihood of our data
    * recall likelihood: $$L(params) = \prod_{y=1} p(x) * \prod_{y=0} (1-p(x))$$
    * this can be simplified by taking $log(likelihood)$ and using fact that log(a*b) = log(a) + log
(b)
    * i.e., $l(params) = \sum_{i=1} y_{i}*log(p(x_{i})) + (1-y_{i})*log(1-p(x_{i}))$
    * if we substitue p(x) with its exponent form then --> $$l(params) = \sum_{i=1} y_{i}*\beta*x_{i} + log(\dfrac{1}{1+exp(\beta*x_{i}))$$

### [Gradient Boosting](https://www.youtube.com/watch?v=StWY5QWMXCw) (recall XGBoost is a specific implementation of Gradient Boosting)
  * similar to adaboost, but typically larger than stumps
  * builds fixed-size trees based on previous trees errors
  * scales all trees by same amount
  * for regression:
    1. grow tree
    2. compute psuedo residual (actual - predicted)
    3. fit tree to psuedo residuals
    4. new predictions are prior + learning_rate*new_tree
  * similar to gradient descent in linear/logistic regression recall that we take the derivative of the loss function with repspect to some params
  * then knowing we want to minimize the loss function, we move in the negative gradient by updating those params
  * in this case we aren't in param-loss function space, we are in prediction-loss function space
  * so, we are taking the derivate of the loss function with respect to the previous prediction, then we are changing the target of our next iteration as a result!
  * instead of finding the $\omega$, $\beta$ **param update to minimize loss**, we are finding the **new target prediction** to minimize overall loss
  * classification:
    * when getting into the details this is quite complicated, but the important things to remember when thinking about motiviation:
      * we are constantly switching in-between log(odds) space and probability space
      * we grow regression trees (and therefore need to use log-odds space!), but when making predictions we want to convert from log(odds) --> p
    * approach:
      1. make an initial guess which turns out to be log(odds) = log(p/1-p), this turns out to be the guess that minimizes log-lilihood (which you can express in terms of prob and log-odds)
      2. compute the gradient of loss with respect to function which truns out to be $observed\\_value - \dfrac{exp(log(odds))}{1+exp(log(odds))}$ which is same as $observed\\_value - probability$. this is also the psuedo-residual. compute these psuedo-residuals for each sample.
      3. fit a regression tree to pseudo-residuals **in the log-odds space**. then, via lots of math we can show that the leaf value for any node that minimizes our overall loss = $\dfrac{\sum residuals}{\sum p*(1-p)}$ for all samples in the leaf node, where $residuals$ are values in the leaf nodes and $p, 1-p$ is the most recent (prior) predicted probability for the sample.
      4. **finally** $prediction = previous prediction + ((learningRate)*(new prediction))$ this is in log-odds space.
      5. to convert new log-odds prediction to probability --> $probability = \dfrac{exp(log(odds)))}{1+e(log(odds))}$

* Feature Importance
  * [COMPLETE THIS SECTION]
