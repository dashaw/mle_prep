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


