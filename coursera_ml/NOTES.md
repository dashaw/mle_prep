## [Course link](https://www.coursera.org/learn/machine-learning/home/welcome)

## Gradient descent

* batch = using all samples for update step

## Vectorization

* remember lower-level detail of how we use vectorization/matrix multiplication 
* e.g., going from $f_{w,b}(x) = w_{1}*x_{1} + w_{2}*x_{2} + b$ --> $f_{w,b}(\vec{x}) = \vec{w} \cdot \vec{x} + b$ 
* able to use the parallel hardware on a normal computer CPU, GPU
* without vectorization
  * for loop: runs sequentially through each time step, one at a time
* with vectorization
  * can get all value from w, x at same time in parallel
  * specialized hardware to add all together
  * scales well with larger datasets
* example: gradient descent with 16 features
  * 16 weights
  * 16 derivatives
  * compute update step for each feature
  * without vectorization: loop through all 16 features
  * with vectorization: parallel processing does this all in one step

## Gradient descent in practice
  * feature scaling: look at two input features with very different scales. If you observe contour plot of cost function, you see it is very tall and small width. gradient descent can end up bouncing back & forth and take a long time to find minimum.
    * if you scale, gradient descent can find direct path more efficiently
  * convergence: easy approach is to keep track of the cost function value for each iteration --> plot over time to see if it is continually decreasing by at least some $\epsilon$
  * if cost value is bounding around --> could be too large learning rate that is bouncing to different low minimum bowls. **with small enough learning rate, should always continually decreasing**
  * i.e., setting alpha to be _very_ small is a debugging step
  * feature engineering: always remember ability to explicitly create cross features (i.e., x1, x2 --> x3 = x1*x2)
  * polynomial regression --> input features to some power (note: feature scaling becomes increasingly important)

## Logistic regression
  * i.e., need function with output between [0, 1]
  * sigmoid function: $g(z) = \dfrac{1}{1+e^{-z}}$
  * if z very big --> g(z) ~1, if z very negative --> g(z) ~1
  * if z = 0 --> g(z) = 0.5
  * so, $f_{w,b}(x) = \dfrac{1}{1+e^{-(wx + b)}}$
  * can have non-linear decision boundaries with polynomial features (i.e., using $x_{1}^2, x_{2}^2$)
  * but if you don't include polynomial features, decision boundary will always be linear

**cost function**
* if we re-used squared error cost for the above $f(x)$ model, it would be non-convex
* log-loss function: $L(f_{w,b}(x)) = -y*-log(f_{w,b}(x)) - (1-y)*log(1 - f_{w,b}(x))$
* if doing this, then cost function will be convex when using this loss function and summing over all samples
* cost function: $$- \dfrac{1}{m} \sum_{i=1}^m -y*-log(f_{w,b}(x)) - (1-y)*log(1 - f_{w,b}(x))$$
