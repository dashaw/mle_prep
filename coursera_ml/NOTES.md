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
