### Courses 
* [NLP Course 1](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/home/week/4)
* [NLP Course 2](https://www.coursera.org/learn/probabilistic-models-in-nlp/lecture/i8pZr/n-grams-and-probabilities)
* [NLP Course 3](https://www.coursera.org/learn/sequence-models-in-nlp/lecture/SgnFd/recurrent-neural-networks)

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

#### Course 3
##### RNNs
* recurrent neural networks
* recall that we typically see these "through time" with repeated blocks, but really the weights we are learning are just for a single NN. Instead, we are continually feeding inputs into the same block "recurrently"
* propagates information through the sentence (for example)
* different architectures
  * 1:1 i.e., single input and single output
  * multi:1 i.e., multi input words and predict good/bad sentiment
  * multi:muli i.e., multi input words and multiple output words like language translation (aka, encoder/decoder)
  * 1:many i.e., image input and output sentence describing image
* loss/cost function: can use same cross-entropy loss function, but this time you'll also want to average not just over all samples, but also through time (in case of vanilla RNN)
* for long sequences of words, the information tends to vanish
* bi-directional = feed information from left->right and right->left, then output for a given time step is combination of the two hidden states fed through an activation function
  * information is ascylic and flows independently (i.e., don't need to first forward propogate left->right then right->, can do both in parallel)

##### GRUs
* gated recurrent units
* uses relevance and update gaes
* RNNs with some additional steps
* has keep/update gates, determines which context to keep
* relevance and update gates

##### LSTM
* why?
  * RNNs: captures dependencies w/in short range, less RAM vs. n-gram models
    * cons: struggles to capture long term dependencies
    * prone to vanishing/exploding gradients
    * backpropogation through time --> chain rule through time = vanishing/exploding gradients
  * solution to vanishing/exploding gradients
    * identity weight matrix with ReLU activation
    * gradient clipping
    * skip connections
* long-term solution memory = solution to issues found in RNNs
* learns what to remember and what to forget
* anatomy: cell state, hidden state, multiple gates
* cell state, hidden state, input
* inside: 1. forget gate (info that is no longer important), 2. input gate (info to be stored), 3. output gate (info to use at current state

##### Siamese networks
* e.g., determine if two questions are duplicates
* architecture: two networks: 1 takes question 1 --> embedding --> lstm --> output, then two ouputs of the two questions take cosine similarity
* one shot learning e.g., using siamese networks to compare similarity between e.g., two signature (1 input = known signature, 1 input = proposed signature) --> compute similarity --> based on this threshold as same or not
