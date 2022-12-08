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
