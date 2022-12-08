### Key steps
1. Setting up the problem
  * broad question typically, so **ask questions**
  * narrow problem space, chalk out requirements
  * goal = arrive at a precision machine learning problem statement
  * example you want to go from "design the Twitter feed" to "given a list of tweets, train an ML model that predicts the probability of engagement of tweets and orders them based on that score."

2. Understand scale and latency requirements
  * latency: e.g., if search engine --> do we want to return the search result in 100 milliseconds or 500 milliseconds?
  * scale of the data: if twitter --> how many tweets would we have to rank according to relevance? what is the input candidate size?

3. Defining metrics
  * help you see if your system is performing well
  * metrics for **offline** testing e.g., AUC, log-loss, precision, recall, nDCG
  * metrics for **online** testing e.g., you might have local (specific to product you are perturbing) and global (relevant to product surfaces outside your own)

4. Architecture discussion
  * think about the components of the system and how data will flow through those components
  * need to reference the **requirements** section above to support architecture decisions

5. Offline model building and evaluation
  * labels: are labels human generated or via user-action?
  * feature engineering: which features will we use? what types? give an idea and example of how we would use a combination of (example) product, user, context, user-product features
  * model: if using funnel approach, you may select simple model at top of funnel and then used NN/trees for down funnel portions. additionally could use a pre-trained SOTA model and perform transfer learning
  * offline evaluation: use aforementioned offline metrics

6. Online model execution and evaluation
  * deploy online and use aforementioned online metrics to understand user-impact. A/B or observational inference.

7. Iterative model improvement
  * consider things like: data drift, concept drift
  * monitoring engineering and predictive performance, if issues then performing debugging
