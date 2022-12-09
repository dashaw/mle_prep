## [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)

### Logistic Regression
* recall, $y^{i} = \sigma (w^{T}x^{(i)} + b)$ where $\sigma(z^{i}) = \dfrac{1}{1+e^{-z^{i}}}$
* loss (error) function: $L(y_{pred}, y) = -(y*log(y_{pred}) + (1-y)log(y_{pred}))$
* cost function = average of loss, goal = find $w$, $b$ that minimize the cost function 

### Exploding/Vanishing Gradients
* if weight values slightly greater than 1 --> you can run into scenario where this slightly greater than 1 number is being put to power of L --> thus large number
* similarly if weights slightly less than 1 --> power of L layers --> thus small number
* vanishing: as we move backward, gradients get smaller and smaller and approach 0, eventually leaving weights of the intial or lower layers unchanged
* exploding: on contrary, gradients get larger and alrger, and taking huge weight updates

**why?**
* on either end of graph, gradients go nearly to 0
* thus, when backpropogation we start to shrink quickly
* similarly if initial weights are huge, then multiplicative nature can cause huge updates

**how to spot**
* vanishing: 
  * higher layer params change significantly while lower layers not at all
  * model weights --> 0
  * learns slowly

* exploding:
  * expoential growth in model params
  * model weights may become so large they go to NaN due to overflow

**solutions**
* exploding gradients: initialize weights with normal distribution and mean 0, or uniform distribution (see Xavier initialization or Glorot initialization)
* use activation functions that do not have saturating gradients:
  * e.g., ReLU = $R(z) = max(0,z)$, but this can suffer from "dying ReLUs where some neurons simply go to 0"
  * e.g., Leaky ReLU $LReLU = max(\alpha * z, z)$
* batch normalization: adding an operating in the model just before or after activiation functionf or each hidden layer, ensure inputs are 0 centered and unit deviation. Does so by evaluating params for the current mini batch --> hence "batch normalization"
