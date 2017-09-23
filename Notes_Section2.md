# Section 2

This section covers the following topics on **Game Playing**:

- Adversarial Search
- Minimax algorithm
- Alpha-Beta Pruning
- Evaluation Functions
- Isolation Game Player

## Review points

- Alpha-beta Pruning
- Expected-Max Algorithm and Pruning quiz

## Reference

- READING:  *AIMA Chapter 5.1-5.2*
- READING:  *AIMA Chapter 5.3-5.4*
- [Korf, 1991, Multi-player alpha-beta pruning](https://www.cc.gatech.edu/~thad/6601-gradAI-fall2015/Korf_Multi-player-Alpha-beta-Pruning.pdf)

## Isolation Game: [An Example](https://boardgamegeek.com/boardgame/1875/isolation)

1. Build a Game Tree: gradually expand the search space
2. For children that cannot be expanded: assign a score for winning/losing state

## Minimax Algorithm:

- Computer tries to **maximize** the score; opponents try to **minimize** the score.
- Min Level: triangle pointing down -- opponents want to minimize the score (minimize the scores coming from the children)
- Max Level: triangle pointing up -- computer want to maximize the score (maximize the scores coming from the children)
- **propagating values up the tree**:
- Branching factor: the width of possible next states to be expended
	- Estimate the possible states in the search tree: $b^d$ notes, $b$ is the average branching factor, $d$ is the depth
	- Average branching factor (run a simple program that randomly play the game and calculate the average branching factor)
- Depth-Limited Search:
	- Only search up to some depth --- stop before too much time has spent
	- Problem: we won't end with the final game state!
	- Solution: create an **evaluation function** for the unfinished state.
		- Evaluate how good a state is.
		- e.g. number of possible moves
	- Given an *evaluation function*, different depth may results in different values, thus different recommended actions.
- Quiescent Search
	- Search deep enough when the recommended action does not change too much.
  - Final(terminal) State Value: The upper limit is arbitrary except that it must be larger than the maximum value of the evaluation heuristic, which is +5 in this case. (The value of the terminal states is defined at 0:42 of the video.)

Pseudocode: MINIMAX

```
function MINIMAX-DECISION(state) return an action
	return argmax(a in ACTIONS(state)) MIN-VALUE(RESULT(state, a))
------------------------------------------------------------
function MAX-VALUE(state) returns a utility value
	if TERMINAL-TEST(state) then return UTILITY(state)
	v = -INFINITY
	for each a in ACTIONS(state) do
		v = MAX(v, MIN-VALUE(RESULT(state, a)))
	return v
-------------------------------------------------------------
function MIN-VALUE(state) returns a utility value
	if TERMINAL-TEST(state) then return UTILITY(state)
	v = +INFINITY
	for each a in ACTIONS(state) do
		v = MIN(v, MAX-VALUE(RESULT(state, a)))
	return v
```

Note: the `MAX-VALUE` function and `MIN-VALUE` function are *mutually recursive* functions. These two functions can be integrated into a single [negamax](https://www.wikiwand.com/en/Negamax#/Negamax_base_algorithm) recursive function.

### Implementation

- See `./sample-code/isolation-game`

- minmax assmptions:
	- Assumption 1: a state is terminal if the active player has no remaining moves
	- Assumption 2: the board utility is -1 if it terminates at a max level, and +1 if it terminates at a min level

## Iterative Deepening (ID)

- General Idea:
  - first, search with `depth == 1`, find the best solution based on *evaluation*
  - save the current best solution
  - then, do the search with `depth == 2`, find the best solution now
  - save the current best solution
  - gradually increase the `depth` during search and save the best solution each time
  - run until out of tolerable time.
- Exponential times
  - binary tree:
    - Level 1: Tree nodes - 1, ID nodes: 1
    - Level 2: Tree nodes - 3, ID nodes: 1 + 3 = 4
    - Level 3: Tree nodes - 7, ID nodes: 1 + 3 + 7 = 11
    - In the end: ID nodes < 2 * Tree nodes
  - let `branch = 2` and `depth = d`, total nodes of the tree $n = 2^{d+1}-1$
  - let `branch = 3` and `depth = d`, total nodes of the tree $n = \frac{3^{d+1}-1}{2}$
  - let `branch = k` and `depth = d`, total nodes of the tree $n = \frac{k^{d+1}-1}{k-1}$
  - so ID doesn't cost more than total nodes
- Horizon Effect:
  - When it is obvious to a human player that the game will be decided in the next move, but that the computer player cannot search far enough into the future to figure out the problem
  - may use a complicated evaluation function
  - trade-off: complicated evaluation takes longer time to compute.
  - e.g. maybe we can use `#my_moves - #opponent-moves`
- Alpha-Beta Pruning
  - As soon as we find a currently good solution, we don't have to search for the rest worse or equally well solution space.
  - We are assuming the goal of our computer player is to play the game, not to keep all equally good move.
  - reduce $b^d$ time to $b^{\frac{d}{2}}$ time, or $b^{\frac{3d}{4}}$ time in random moves.

## Some other tricks in the 5x5 isolation-game

1. Use symmetry to reduce the space: Some states are equivalent because
    - They are symmetrical relative to the center (e.g. (0, 0) == (4, 4))
    - They are symmetrical relative to the diagonal (e.g. (0, 1) == (1, 0))
    - They are symmetrical relative to the main axes (e.g. (0, 0) == (0, 4))
    - **TRICK**: before expanding a state, see whether some symmetrical counterparts have been searched before.    
2. If two players are separated -- we can just solve that directly by counting possible moves.
3. Winning Solution
    - If player 1 first move to the center of the board, and if player 2 first move to a place where player 1 can find reflection: player 1 can always win by reflect and mimic player 2's move.
    - If player 2 moves such that player 1 cannot find a reflection: player 2 wins

## 3-Player Isolation

For multi-player game, we don't use minimax, we use **MAXN** strategy: only calculate from the perspective of each player.

- First level: we choose the max-value from player-1's perspective
- Second level: we choose the max-value from player-2's perspective
- Third level: we choose the max-value from player-3's perspective
- Forth level: we choose the max-value from player-1's perspective
- keep on: we only use a state from the current player's perspective

**Alpha-Beta pruning** in multi-player case

- All values must be *non-negative*

## Probabilistic Games: Expected Max

When the search tree has the probability to expand, we need to use **Expected Max** algorithm.

We now need to calculate the expectation of the evaluation function and then do mini-max, we can do some pruning similarly.
