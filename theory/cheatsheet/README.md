## Cheatsheet
* source = primarily Burkov's [Machine Learning Engineering](http://www.mlebook.com/wiki/doku.php)
* other
  *  [complete guide to recommender system tutorial with sklearn, keras](https://towardsdatascience.com/a-complete-guide-to-recommender-system-tutorial-with-sklearn-surprise-keras-recommender-5e52e8ceace1)

### Training
* **data bias**: many forms, but e.g., we are training recsys model using historical data which is biased by the prior recommendation system as those are the impression/engagement samples users saw. **solution** --> small sample of users receive random recommendations.
* **leakage**: example: when a feature implicitly encodes the target such as predicting yearly salary, but monthly salary is a feature

#### Feature Engineering:
* normalization
* standardization
* data imputation
* binning continuous features
* log transform feature: primarily used to convert a skewed distribution to a normal distribution/less-skewed distribution
* bag of words: (aka n-grams with n = 1), get unique words in all documents, assign each word a vector position, represent sample with 1's in the position of the contained word.
  * e.g., ['harlow likes many treats', 'darren likes to treat harlow'] --> ['darren','likes','harlow','treat','treats'] --> [[0,1,1,0,1], [1,1,0,0,1]]
  * obviously you can see how this extends to n-grams where instead the input to all unique combos are things like ['darren likes','likes to','to treat','treat harlow']
  * no concept of order

* word embeddings: i.e., learn dense representations during training or from another network


#### Metrics
* $precision = \dfrac{TP}{TP+FP}$, how many of our predictions are correct?
* $recall = \dfrac{TP}{TP+FN}$, how many did we get right vs. how big is the class 1 pie
* $F1 = 2*\dfrac{precision*recall}{precision+recall}$
* $accuracy = \dfrac{TP+TN}{TP+TN+FP+FN}$
* $TPR = \dfrac{TP}{TP + FN}$, rate of true positives, aka our true positives vs. all positive class examples (**same as recall**)
* $FPR = \dfrac{FP}{FP + TN}$, rate of false positives, aka our false positives vs. all negative class examples

##### Ranking
* discount cumulative gain = $\sum_{for all i positions} \dfrac{rel_{i}}{log_{2}(i+1)}$
* normalized discount cumulative gain = $\dfrac{DCG}{IDCG}$
  * i.e., compute dicount cumulative gain for the ideal ordering case and call this ideal discount cumulative gain $IDCG$

#### Hyperparam Search
* grid search (basic approach)
* random search

#### Initialization Strategies
* random normal is an easy standard (i.e., initialize weights/bias to be from random unit-normal distribution)

#### Regularizaiton
* l1 vs. l2
* l1 = $\sum |w|$
  * feature selection because it drives weights to 0, to understand this look at grid of l1 and l2 for same bias generated and observe that the cost function intersects with the pointy part of l1 which happens to be typically in spots where at least 1 axis is = 0
  * another way to think of it is like so, in minimizing a cost function if an example weight is 0.05 then when this weight is squared it gets even smaller, thus it contribues less to the overall cost and there is less value in making it 0
  * another way is also to view the gradients of the two and see that for l1 the gradient is +/- 1 thus we step in constant direction, while for l2 derivative = w and so we move in smaller steps
  * [l1/l2 image](https://i.stack.imgur.com/sBFdb.png)
* l2 = $\sum (w)^2$
* dropout
* pruning
* batch normalization between layers = standardizes outputs of neurons before input to next layer (0 mean and 1 variance) --> faster and more stable training
* early stopping

### Deployment
* data drift: distribution of features are skewed between train and serve

* concept drift: underlying mapping of X-->Y has changed between train and serve, e.g., prior users engaged with content of type A and now they don't like A and prefer content of type B

### Iterative Updates
* warm-start (i.e., using recent samples and using prior model state to continue learning) typically performs worse than cold start (i.e., using all new/old samples and weights/bias from "scratch"). difficult problem that has its own body of research.
* current solutions = shrink and perturb --> shrink weights/bias by value between 0 and 1 --> applying random gaussian noise --> continue learning using new samples
* **new data beats clever features** i.e., don't let models be stale

#### Modes of Serving

**Serving in Batch Mode**
A model is usually served in batch mode when it is applied to large quantities of input data. One example could be when the model is used to exhaustively process the data of all users of a product or service. Or, when it systematically applies to all incoming events, such as tweets, or comments to online publications. Batch mode is more resource-efficient compared to an on-demand mode, and is employed when some latency can be tolerated. When served in batch mode, the model usually accepts between a hundred and a thousand feature vectors at once. Experiment to find the optimal batch size for speed. Typical sizes are powers of two: 32,64,128,etc

**Serving on Demand to a Human**
* Six steps of serving the model **on demand**:
  1. validate the request
  2. gather the context
  3. transform the context into model input
  4. apply the model to the input and get the output
  5. make sure output makes sense
  6. present the output to the user

* feature extractor transform context into the model input

<img src="images/on_demand_serving.png" alt="drawing" width="700"/>

#### Recommender Systems
* Example specific architectures: neural collaborative filtering
  * [keras tutorial](https://keras.io/examples/structured_data/collaborative_filtering_movielens/)

<img src="images/neural_collaborative_filtering.png" alt="drawing" width="700"/>

#### Assumptions
* linear regression: linear relationship between independent x's and dependent y, residual are independent (no correlationship b/w consecutive residuals), homoscendasticty (residuals have constant varaince through x), residuals are normally distributed
  * independence = mostly relevant for time-series data, don't want there to be a pattern for consecutive residuals (e.g., shouldn't steadily grow over time)
  * heteroscedasticty = would mean varaiance of regression coefficient increases, but model does not pick it up = likely to declare a term statistically significant
  * normality
* logistic regression
  * binary response
  * independent observations
  * no multicolinearity
  * no extreme outliers
  * linear relationship between explanatory variables and the logit of the response

#### Misc notes
* $error = bias + variance + noise$
* boosting based on weak learners (high bias, low varaince), reduces error mainly by reducing bias
* random forest reduces error in the opposite way: reducing variance while leaving the bias unchanged
  * uses modification of bagging to build de-correlated trees and then averages output. bias for random forest is the same as that of any individual tree = has low bias. on the other hand it is fine if these each have high variance, because when averaging the trees it reduces variance
