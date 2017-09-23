# Section 1

This section covers the following topics:

- Introduction to AI
- Search, Heuristic, and Constraint Propagation to solve Sudoku

## Introduction

- [Monte Carlo Tree Search](https://www.wikiwand.com/en/Monte_Carlo_tree_search)
- [Deep Blue Paper](https://pdfs.semanticscholar.org/ad2c/1efffcd7c3b7106e507396bdaa5fe00fa597.pdf)
- [Alpha Go Paper](https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf)

## Apply AI to Sudoku

- [Peter Norvig's post](http://norvig.com/sudoku.html)
- Two topics:
	1. Constraint Propagation: Constraint Propagation is all about using local constraints in a space (in the case of Sudoku, the constraints of each square) to dramatically reduce the search space. As we enforce each constraint, we see how it introduces new constraints for other parts of the board that can help us further reduce the number of possibilities
	2. Search
- Representation of Sudoku: Rows and Columns
	1. The rows will be labelled by the letters A, B, C, D, E, F, G, H, I.
	2. The columns will be labelled by the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9. Here we can see the unsolved and solved puzzles with the labels for the rows and columns.
	3. The 3x3 squares won't be labelled, but in the diagram, they can be seen with alternating colors of grey and white.
- Representation of Sudoku: Boxes, Units and Peers
	1. The individual squares at the intersection of rows and columns will be called **boxes**. These boxes will have labels 'A1', 'A2', ..., 'I9'.
	2. The complete rows, columns, and 3x3 squares, will be called **units**. Thus, each unit is a set of 9 boxes, and there are 27 units in total.
	3. For a particular box (such as 'A1'), its **peers** will be all other boxes that belong to a common unit (namely, those that belong to the same row, column, or 3x3 square).

- Strategy
	- A) Elimination (Eliminate impossible solution)
	- B) Only Choice (Fill in determined choices based on constrains)

## AI

1. Heuristic:
	- some additional piece of information - a rule, function, or constraint - that informs an otherwise brute-force algorithm to act in a more optimal manner.
2. Find a good Representation
	- Tic-Tac-Toe: use a whole board as a representation.
3. Pruning the search tree
4. Adversarial search: Mini-max algorithm

### Define Intelligence

- Environment
	- Fully observable v.s. Partially observable
	- Deterministic v.s. Stochastic
	- Discrete v.s. Continuous
	- Benign v.s. Adversarial
- Agent
- State
	- goal state, current state
- Perception (sensors)
- Cognition (internal processing)
- Actions

> An intelligent agent is one that takes actions to maximize its expected utility given a desired goal.

- Rational behavior v.s. Bounded Optimality
	- 60% times beating the opponents
	- second or third optimal route


## Extra. Resume and Job

- [Edit Udacity Profile](https://classroom.udacity.com/profiles/u/edit)
- [Nanodegree Career Services](https://career-resource-center.udacity.com/start-your-job-search/nanodegree-career-services)
- [Get Hired, suggestions from Udacity](https://www.udacity.com/get-hired)
