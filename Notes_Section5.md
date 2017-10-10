# Section 5

This section covers the following topics:

- Probability
- Bayes Nets
- Inference on Bayes Nets
- Hidden Markov Model

## Referece

- READING:  *AIMA Chapter 13*
- [Rabiner's Tutorial](http://www.cs.ubc.ca/~murphyk/Bayes/rabiner.pdf) and [Errata](http://alumni.media.mit.edu/~rahimi/rabiner/rabiner-errata/)
- [Thad Starner's MS Thesis](http://dspace.mit.edu/bitstream/handle/1721.1/29089/32601581-MIT.pdf)
- [HTK toolkit](http://htk.eng.cam.ac.uk/)
- [The Fundamentals of HTK](http://speech.ee.ntu.edu.tw/homework/DSP_HW2-1/htkbook.pdf) or [HTML version](http://www.ee.columbia.edu/ln/LabROSA/doc/HTKBook21/HTKBook.html)
- [Hidden Markov Models for Speech Recognition(BOOK)](http://www.amazon.com/Hidden-Recognition-Edinburgh-Information-Technology/dp/0748601627)
- [HMM used in genetics (slides)](http://www.cs.columbia.edu/4761/notes07/chapter4.1-HMM.pdf)
- Sebastian Thrun & Peter Norvig's course
		- [HMM and Kalman Fiters](https://classroom.udacity.com/courses/cs271/lessons/48734405/concepts/last-viewed)
		- [NLP I](https://classroom.udacity.com/courses/cs271/lessons/48641663/concepts/last-viewed)
		- [NLP II](https://classroom.udacity.com/courses/cs271/lessons/48734403/concepts/last-viewed)
- Segmentally Boosted HMM
		- [SBHMM project at Georgia Tech](http://www.cc.gatech.edu/cpl/projects/sbhmm/)
		- [HTK part](http://htk.eng.cam.ac.uk/)
		- [Gesture and Activity Recognition Toolkit](https://wiki.cc.gatech.edu/ccg/projects/gt2k/gt2k)
		- [Pei Yin's Dissertation on using SBHMM]https://smartech.gatech.edu/handle/1853/33939)
- HMMs for Speech Synthesis
		- [Junichi Yamagishi’s An Introduction to HMM-Based Speech Synthesis](https://wiki.inf.ed.ac.uk/twiki/pub/CSTR/TrajectoryModelling/HTS-Introduction.pdf)
		- [Heiga Zen’s Deep Learning in Speech Synthesis](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41539.pdf)
		- [DeepMind's WaveNet](https://deepmind.com/blog/wavenet-generative-model-raw-audio/)

## Probability

>The **Bayes Network** is a compact representation of a distribution over this very large joint probability distribution of all of these variables

Steps:
- Specify a model
- Observe data
- Compute the probability

Some Advanced models built on Bayes Networks
- Particle Filters
- Hidden Markov Models
- MDP's
- POMDP's
- Kalman Filters


Total Probability: $P(Y) = \sum_{i}P(Y|X=i)P(X=i)$

## Bayes Networks

> Bayes Networks: Define probability distributions over graphs of random variables

A simple network:

> A -> B

where B is *observable* and A is *not observable*

- Causal Reasoning
	- P(B | A)
	- P(B | ~A)
- Diagnostic Reasoning
	- P(A | B)
	- P(A | ~B)
- How many parameters does it take to specify the **entire** joint probability within A and B
	- 3 parameters
		1. P(A), from which we can calculate P(~A)
		2. P(B | A), from which we can calculate P(~B | A)
		3. P(B | ~A), from which we can calculate P(~B | ~A)
- Calculate Bayes: we can defer the normalizer calculation later.
- Conditionally independent
	- $P(T_2 | C, T_1) = P(T_2 | C)$
	- given $C$, the knowledge of $T_1$ provide no information for $T_2$
	- however, $B \perp C | A$ **does NOT imply** $B \perp C$
		- example: $A$ is canter, $B, C$ are tests. Without knowing $A$, the knowledge of $B$ test to be positive will increase the probability of $A$ as having a cancer, thus $C$ has a higher probability to be positive.
- Conditional dependence
	- Two causes are independent
	- By observing the effects of these causes, they become dependent
	- *effects* can tell something about *causes*, and make them dependent
- **NOTE:**
	1. absolute independence **does NOT** imply conditionally independence
		- *explain in the future*
	2. conditionally independence **does NOT** imply absolute independence
		- previous item has shown
	3. If two independent causes of a result, one cause does not inform the other cause.
	4. **Explaining away**: If we know the results and one cause happens, the probability of another cause happens will **decrease**.
		- If either *sunny(S)* or *raise(R)* can cause *happy(H)*, and I know someone is *happy*. If I also know it is *sunny*, then I would think this person is happy because it is sunny, and less likely because s/he got a raise: $P(R|H,S) < P(R|H)$
		- Seeing one cause of the effect can lower the probability of other causes happens.
- Advantage: help to factorize the join probability and reduce the number of parameters.
 	- $P(A,B,C,D,E)$ with each as a binary variable needs $2^5 - 1 = 31$ values in probability
	- $P(A,B,C,D,E) = P(A)P(B)P(C|A)P(D|B)P(E|C,D)$ only needs 10 values
		- $P(A)$ needs one parameter, $P(-A) = 1 - P(A)$; same as $P(B)$
		- $P(C|A)$ needs two parameter, $P(C|A)$ and $P(C|-A)$, and we can calculate $P(-C|A), P(-C|-A)$
		- $P(E|C,D)$ needs 4 parameters
- **D-Separation**
	- any two variables are independent if they are not linked by just unknown variables

## Inference in Bayes Nets

- Types of variables
	- **Evidence** variables: variables that we know the values of
	- **Query** variables: Variables that we want to find out the values of
	- **Hidden** variables: Anything that is neither evidence nor query is known
- Inference on Bayes Nets:
	- The answer is going to be the join probability of all query variables
	- we all it **posterior distribution** given evidence
	- $P(Q_1, Q_2 ... | E_1 = e_1, E_2 = e_2, ...)$
	- or we can get MAP: $\text{argmax}_{q}P(Q_1 = q_1, Q_2 = q_2, ...| E_1 = e_1, ...)$
- Enumeration:
	- $P(+b | +j, +m) = \frac{P(+b, +j, +m)}{P(+j, +m)} = \sum_e\sum_a\frac{P(+b, +j, +m, e, a)}{P(+j, +m, e, a)}$
		- we need to enumerate values of **hidden** variables
	- If there are tons of variables, we need to **speed up enumeration**
		1. pull terms out of summation
		2. maximize independence: by knowing the **evidance** variables, hidden variables and other variables are not independent as they used to be.
- Causal Direction
	- Write the Bayes Nets in a Causal Direction
- Variable Elimination (Bayes Net is still *NP Complete*)
	1. Jointing Factors: make a joint distribution table. $P(R, T) = P(R)P(T|R)$
	2. Elimination $P(T) = \sum_R P(R,T)$
	3. Repeatedly, we can always marginalize the distribution and eliminate variables
- Approximate Inference: SAMPLING!
	- we sample according to the conditionally probability table
 	- rejection sampling: we reject samples that do not match the inference we need
		- For a event that has small probability, we may end up rejecting LOTS OF samples
		- *NOT efficient*
		- samples are *independent* of each other
 	- Likelihood Weighting:
	 	- say we only want $P(B| +a)$, we can fixed $A = +a$, and only sample $B$, but we have a problem: the probability is **not consistent** any more.
		- we weight sample with the likelihood (get the likelihood from the table)
	- Gibbs Sampling
		- samples are dependent on each other!

## Hidden Markov Model

- Dolphin whistles
	- delta frequency (only care about the successive differences) -- ignore the absolute magnitude
	- time warping -- deal with signals extended or contracted in time
		- Euclidean Distance: padding and calculate Euclidean distances
		- Dynamic Time Warping: matching two signals in as in 2D
			- Sakoe Chiba Bounds
			- [Further reading](http://wearables.cc.gatech.edu/paper_of_week/DTW_myths.pdf)

- HMM: good for pattern recognition in time series

### Representation of HMM

- $X_i$ represents a frame of data
- $E_i$ represents the output of the state
- $X_i$ transits according to Markov Chain, each $X_i$ has the output as $E_i$

- output distribution: the distribution from $X_i$ generates $E_i$
- transition probability between $X_i$ and $X_{i + 1}$
- self-loop: a state can stay at its own state $X_i$ to $X_i$
- use *dummy state* to enter the first state

### Viterbi Algorithm

We can layout a $n(state) \times n(time)$ grids and map out the transition probability as well as the probability of each observation.

Then we can use Dynamic Programming to calculate the maximum probability path from start to the end.
- The probability is the `product` of all the probability along the path, including both **transition probability** and **the probability of an observation**.
- In practice, we use `sum log(prob)`
- in the end we get: `p(observation | model)`

### Recognization

For different models, we have different `p(observation | model)`, and we pick the model that can maximize the probability

### HMM Training

- 5 - 12 examples are minimal for training each model.
- A) get the transition probability
	- different length of signals -- cut them each into similar segments (three states, then three segments)
	- average the length of each segments can provide information for the transition probability (e.g. `average length = 4` --> `p = 0.25` to go to the next state)
	- then get the self-loop transition probability
- B) get the observation distribution
	- for all the data in each segment, we can use mean/std to construct a probability distribution for `p(output | state)`
- iterative update A), B)
	- set transition probability and update the observation distribution
		- for each observation: we need to recalculate which state it belongs to by comparing neighboring `p(output | state)`, and assign to the MLE state
		- thus, we update the transition segmentation based on the observation distribution
	- set observation distribution and update the transition probability
	- until converge
- quite similar to EM or K-means algorithm in update
- **Baum Welch** re-estimation
	- similar to EM
	- forward-backward process
- Multidimensional distribution and Mixture Gaussian distributions

### HMM topology

- linear chain state
- loop in the model chain
- multiple model for the same signal of different variants -- we can increase the our vocabulary
- even more complicated graph / network

### Stochastic Beam Search

- prune some low probability path. But we don't want to drop the low probability path entirely because later it may be good
- **keep the paths randomly in proportion with their probability**

### Context Training

- a phrase of signs is different from individual word signs.
- transition between words may be combined in sign languages.
- instead of training on each single word, we make a combined *phrase* model that train on a whole phrase (e.g. I NEED CATS).
- when training:
	- first divide between each signs in a phrase
	- then divide the data within a sign
- error rate can drop in half

### statistical grammar

- use statistical regularities among word transition
- error rate can drop to 1/4

### State Typing

- Two models of signs may share some part of the states

### Segmentally Boosted HMMs

- Align the model and data
- Boost the model by asking which features help most to differentiate the data from a chosen state versus the rest of the state
- Weight the dimensions appropriately in the HMM
