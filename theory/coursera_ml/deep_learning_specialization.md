## [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)

### Logistic Regression
* recall, $y^{i} = \sigma (w^{T}x^{(i)} + b)$ where $\sigma(z^{i}) = \dfrac{1}{1+e^{-z^{i}}}$
* loss (error) function: $L(y_{pred}, y) = -(y*log(y_{pred}) + (1-y)log(y_{pred}))$
* cost function = average of loss, goal = find $w$, $b$ that minimize the cost function 
