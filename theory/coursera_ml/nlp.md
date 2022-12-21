### Courses 
* [NLP Course 1](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/home/week/4)
* [NLP Course 2](https://www.coursera.org/learn/probabilistic-models-in-nlp/lecture/i8pZr/n-grams-and-probabilities)

#### Course 1
##### Locality sensitive hashing
* given kNN doing N comparisons for a given eval sample, this is one way to simplify
* create random places in the vector space
* determine the side for which a given data point (for all data points) lies on for each plane
* i.e., for one sample and 5 planes we will have a vector where 0 means one side, 1 means other side of plane [0, 0, 1, 0, 0]
* then combine these to form $hash = \sum_{i\\ for\\ all\\ planes} 2^{i} * h_{i}$
* now, at evaluate time, compute the hash of your sample and perform kNN for samples in that hash
* losing some precision, but more efficient

#### Course 2
##### N-grams
* an N-gram is a sequence of N words
  * corpus: I am happy because I am learning
    * unigrams: {I, am, happy, because, learning}
    * bigrams: {I am, am happy, happy because ...}
* after computing bi-grams and uni-grams, we can then use a basic forumla to compute things such as P(am | I) for sentence completion via:
  * $P(am | I) = \dfrac{P(I\\ am)}{P(I)}$
  * i.e., a variation of $P(A,B) = P(B|A)*P(A)$

##### CBOW
* example of creating word embeddings from scratch using CBOW architecture
* 1 hidden layer with activation function = ReLU
* Oupter layer with softmax activation predictions
* Using cross entropy loss $J = - \\sum\limits_{k=0}^V y_{k}*log(\hat{y}_{k})$
