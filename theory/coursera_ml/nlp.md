### Courses 
* [NLP Course 1](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/home/week/4)


#### Locality sensitive hashing
* given kNN doing N comparisons for a given eval sample, this is one way to simplify
* create random places in the vector space
* determine the side for which a given data point (for all data points) lies on for each plane
* i.e., for one sample and 5 planes we will have a vector where 0 means one side, 1 means other side of plane [0, 0, 1, 0, 0]
* then combine these to form $hash = \sum_{i\\ for\\ all\\ planes} 2^{i} * h_{i}$
* now, at evaluate time, compute the hash of your sample and perform kNN for samples in that hash
* losing some precision, but more efficient
