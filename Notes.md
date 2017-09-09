## 1. Introduction

- [Monte Carlo Tree Search](https://www.wikiwand.com/en/Monte_Carlo_tree_search)
- [Deep Blue Paper](https://pdfs.semanticscholar.org/ad2c/1efffcd7c3b7106e507396bdaa5fe00fa597.pdf)
- [Alpha Go Paper](https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf)

## 2. Resume and Job

- [Edit Udacity Profile](https://classroom.udacity.com/profiles/u/edit)
- [Nanodegree Career Services](https://career-resource-center.udacity.com/start-your-job-search/nanodegree-career-services)
- [Get Hired, suggestions from Udacity](https://www.udacity.com/get-hired)

## 3. Conda

- [Conda Documentation](https://conda.io/docs/user-guide/tasks/index.html)
- [Conda Myth and Misunderstanding](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)

## 4. Apply AI to Sudoku

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

### Python Notes

1. `assert` function
2. `value = [candidate if s == '.' else s for s in grid]`