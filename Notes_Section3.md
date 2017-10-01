# Section 3

This section covers the following topics on **Search**, **stochastic search**, and **constraint satisfaction**:

- Search (BFS, DFC, Cheapest-first, A*)
- Random search (random start, simulated annealing, genetic algorithms)
- Backtracking and its optimization


## Reference

- [Korf, 1997. Finding Optimal Solutions to Rubik's Cube Using Pattern Databases](https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf)
- [God's Number is 26 in the Quarter-Turn Metric.](http://www.cube20.org/qtm/)
- [Random Optimization](https://classroom.udacity.com/courses/ud741/lessons/521298714/concepts/5344086080923)
- READING:  *AIMA Chapter 5.3-5.4*
- READING:  *AIMA Chapter 6*

## Define a Problem

- Initial State -> (S0)
- Action (s) -> {a1, a2, ...}
  - action depend on State
  - action does not depend on the State
- Result (s,a) -> s'
- Goal-test(s) -> True / False
- Path Cost (s_i -> a_j -> s_{i+1} -> a_{j+1} -> s_{i+2}) -> cost value (n) where i = 0, 1, ...; j = 1, 2, ...
- Step Cost (s, a, s') -> n


## Search algorithm
### 1. Breadth-First Search (Shortest First Search)

- Quite familiar already...
- Well, tree-search doesn't consider the visited states, graph-search consider the visited states and do not visit them again
- Search stop when the target is in **frontier**
- **QUEUE** is good for the BFS
- it is **complete**: reach the goal even if the search tree is infinite

### 2. Uniform Cost Search (Cheapest First Search)

- Similar to BFS
- When expand, always expand the **lowest total cost** in the frontier set.
- When update, always calculate the cumulative total cost.
- Search stop when the target becomes **explored**
- Need a **Priority QUEUE** for the search
- it is **complete**: reach the goal even if the search tree is infinite

### 3. Depth-First Search

- Quite familiar
- Each time frontier is only expanded in one more state
- it is **NOT complete**: may not reach the goal if the search tree is infinite

### 4. Greedy Best-First

- In addition to 1) and 2), A* adds an **estimate** of the distance *between the start and the end state*
- greedy: always expand the state with **minimal estimated distance**

### 5. A* Search

- `f = g + h`
    - g(path) = path cost
    - h(path) = h(s) = estimated distance to the goal: **heuristic functions**
    - the cost so far + the estimated cost in the future
- also called **best estimated total path cost first search**
- `h(path)` function is an art to Define
    - A* will find the optimal solution **GIVEN a specifically defined function `h`**
    - Requirement: if `h(s) < true cost`
    - that is: **h should never overestimate distance to goal**
    - `h` is *optimistic* to find the best solution
    - `h` is *admissible* to use it to find the lower cost path
- Compare multiple `h` functions
    - if for every state, `h2 >= h1`, and `h1`, `h2` are all admissible
        - `h2` gets us closer to the perfect heuristic
        - `h2` at least the same number of nodes **or fewer**.

## State Space

We need to calculate / estimate the state space of the problem

e.g.
- Route searching: states are cities on the graph

Adding new operators between the states can help to generate `heuristic` functions

## Problems that can be solved with Search

1. The domain must be **fully observable**
    - must be able to see what initial state we start out with.
2. The domain must be **known**
    - must know the set of available actions to us
3. The domain must be **Discrete**
    - must be a finite number of actions to choose from
4. The domain must be **Deterministic**
    - must know the result of taking an action
5. The domain must be **static**
    - must be nothing else that can change the world other than our own action

## Non-deterministic algorithms

**NOTE:** due to different convention, maximum / minimum may be exchanged ...

- NP problem: non-deterministic polynomial time
- NP hard: non-polynomial problems about as hard as each other or NP hard
    - e.g. traveling salesman: exponentially difficult as the number of cities

- N-queens heuristic function
    - given the current state, we want to move a **single queen** up or down in the column that decrease the most numbers of attack
    - we want to keep iterating until we reach our goal of having zero attacks
    - but meet local minimum

## Hill Climbing

- essentially the same as gradient descend
- step size cannot be too large (may overlook the local maximum/minimum, or oscillation), cannot be too small (too long search)

## Random Restart

restart the initial state randomly for each new epoch, and search until a local minimum is found -- hope for the global minimum

- improvements:
    - taboo algorithm: record the states that have been searched before, and don't allow the new search to move into those states (don't do repeated work)
    - stage algorithm: save all the local minima that have been found and try to get an approximation of the function landscape.  

## Simulated Annealing

```
for t = 1 to \infty do
  T <- schedule(t)              # T for Temperature
  if T = 0 then return current
  next <- a randomly selected successor of current
  if delta_E > 0                # energy going from current to next
    then current <- next
    else current <- next only with probability \exp(delta_E / T)
```

- If `T` is high: $\exp^{\delta_E/\infty} = 1$
    - so in the beginning there are lots of random walk
- If `T` is `0` (or actually some value very small, e.g. `0.01`): $\exp^{\delta_E/0.01}$
    - if $\delta_E < 0$, $\exp^{\delta_E/0.01} => 0$
    - if $\delta_E > 0$, we may move to a better solution (moving to global maximum)
- We start with a high `T` and gradually decrease `T`

### local beam search

- start with generating `k` particles
- each iteration: we look at the neighbors of these `k` particles, and keep the `k` best ones for next generation
- if any particle reaches the global maximum -- terminate the search.

## Genetic Algorithms

- select candidate parent states
- calculate the fitness functions of all these states (need some **evaluation functions**)
- generated parents based on the fitness of all candidates
- do **crossover** to breed children states  
    - part of the children coming from one parent state
    - part of the children coming from another partent state
- do **mutation** in the children
    - for each digit (symbol) of a children state, we have a small probability that it will change into a random digit (symbol)
- need to report: **how many generations are needed for stable results**


## Constraint satisfaction

- unitary, binary, or multivariate constraints
- states have constraints between each other
- structured Constraint satisfaction problem:
    - separated the independent cliques
    - if no loop, we can make it as a tree by choosing a variable as root
    - we can condition the graph with some fixed value, and make the remaining part as a tree

## Backtracking search

- try and re-treat
- optimization:
    1. **least constraining value**: choose the variable that **rules out the fewest values** in the remaining variables
    2. **minimum remaining values (MRV)**: choose the variable with the **fewest legal values**
    3. **Degree Heuristic**: choose the variable with the **most constraints** on remaining variables
    4. **forward checking**: for each possible assigned value, we check the possible remaining values before we assign the value
    5. **constraint propagation**: we can propagate the constraints repeatedly to cut the search space
        - *arc consistency*: a variable in a constraint satisfaction problem is arc consistent w.r.t. another variable if there is some value still available for the second variable, after we assign a value to the first variable. If all variable satisfy this, the network is arc consistent.
- save deep searching, but more computation at each search step.
