# Section 5

This section covers the following topics:

- Probability
- Bayes Nets
- Inference on Bayes Nets
- Hidden Markov Model

## Probability

READING:  *AIMA Chapter 13*

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

Working with time series
