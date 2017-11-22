# Part 1 - Planning Problems

Results of Uniformed Planning

## Metrics

1. breadth first search (BFS)
2. depth first graph-search (DFS)
3. uniform cost search (UCS)


### `air_cargo_p1`

| Search    | # Node Expansions | # Goal Tests  | Time Elapsed  | Plan Length   |
|:---------:|:-----------------:|:-------------:|:-------------:|:-------------:|
| BFS       |       43          |       56      | 0.026s        |   6           |
| DFS       |       21          |       22      | 0.012s        |   20          |
| UCS       |       55          |       57      | 0.030s        |   6           |

### `air_cargo_p2`

| Search    | # Node Expansions | # Goal Tests  | Time Elapsed  | Plan Length   |
|:---------:|:-----------------:|:-------------:|:-------------:|:-------------:|
| BFS       |       3346        |      4612     | 15.11s        |   9           |
| DFS       |       107         |      108      | 0.33s         |   105         |
| UCS       |       4853        |      4855     | 11.32s        |   9           |

### `air_cargo_p3`

| Search    | # Node Expansions | # Goal Tests  | Time Elapsed  | Plan Length   |
|:---------:|:-----------------:|:-------------:|:-------------:|:-------------:|
| BFS       |       14120       |      17673    | 121.96s       |   12          |
| DFS       |       292         |      293      | 1.22s         |   288         |
| UCS       |       18223       |      18225    | 48.5s         |   12          |

# Part 2 - Domain-independent heuristics

## Metrics

1. astar_search h_1 (A*H1)
2. astar_search h_ignore_preconditions (A*IP)
3. astar_search h_pg_levelsum (A*PG)


### `air_cargo_p1`

| Search    | # Node Expansions | # Goal Tests  | Time Elapsed  | Plan Length   |
|:---------:|:-----------------:|:-------------:|:-------------:|:-------------:|
| A*H1       |       55          |       57      | 0.019s        |   6           |
| A*IP       |       41          |       43      | 0.022s        |   6          |
| A*PG       |       11          |       13      | 0.385s        |   6           |

### `air_cargo_p2`

| Search    | # Node Expansions | # Goal Tests  | Time Elapsed  | Plan Length   |
|:---------:|:-----------------:|:-------------:|:-------------:|:-------------:|
| A*H1       |       4853        |      4855     | 6.56s        |    9           |
| A*IP       |       1450        |      1452     | 2.42s         |   9         |
| A*PG       |       86        |      88     | 35.48s        |   9           |

### `air_cargo_p3`

| Search    | # Node Expansions | # Goal Tests  | Time Elapsed  | Plan Length   |
|:---------:|:-----------------:|:-------------:|:-------------:|:-------------:|
| A*H1       |     18223        |    18225      |   29.60s      |   12          |
| A*IP       |      5040        |    5042       |   9.46s       |   12          |
| A*PG       |      316        |     318        |  176.68s      |   12          |

### Optimal Solutions for problem 1:

BFS:

```
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)
```
DFS

```
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Load(C2, P1, JFK)
Fly(P1, JFK, SFO)
Fly(P2, SFO, JFK)
Unload(C2, P1, SFO)
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Load(C2, P2, SFO)
Fly(P1, JFK, SFO)
Load(C1, P2, SFO)
Fly(P2, SFO, JFK)
Fly(P1, SFO, JFK)
Unload(C2, P2, JFK)
Unload(C1, P2, JFK)
Fly(P2, JFK, SFO)
Load(C2, P1, JFK)
Fly(P1, JFK, SFO)
Fly(P2, SFO, JFK)
Unload(C2, P1, SFO)
```

UCS

```
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Unload(C1, P1, JFK)
Unload(C2, P2, SFO)
```

### Optimal Solutions for problem 2:

BFS:

```
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Load(C3, P3, ATL)
Fly(P1, SFO, JFK)
Unload(C1, P1, JFK)
Fly(P2, JFK, SFO)
Unload(C2, P2, SFO)
Fly(P3, ATL, SFO)
Unload(C3, P3, SFO)
```

DFS:

```
Fly(P3, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P3, JFK, SFO)
Fly(P2, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P3, SFO, ATL)
Fly(P1, ATL, JFK)
Fly(P3, ATL, JFK)
Load(C2, P3, JFK)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P3, SFO, ATL)
Fly(P2, ATL, JFK)
Unload(C2, P3, ATL)
Fly(P3, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P3, JFK, SFO)
Fly(P2, ATL, SFO)
Fly(P1, SFO, ATL)
Fly(P3, SFO, JFK)
Fly(P1, ATL, JFK)
Load(C1, P2, SFO)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P1, ATL, SFO)
Fly(P3, JFK, ATL)
Unload(C1, P2, JFK)
Fly(P3, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P1, SFO, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, JFK)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Load(C1, P3, JFK)
Fly(P3, JFK, ATL)
Fly(P2, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, JFK, ATL)
Fly(P2, ATL, JFK)
Load(C3, P1, ATL)
Fly(P1, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P1, JFK, SFO)
Fly(P2, ATL, SFO)
Fly(P3, SFO, ATL)
Fly(P1, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P1, ATL, JFK)
Unload(C3, P1, JFK)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P2, SFO, ATL)
Fly(P3, SFO, ATL)
Fly(P2, ATL, JFK)
Fly(P3, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P2, JFK, ATL)
Unload(C1, P3, JFK)
Fly(P1, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P3, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P3, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P2, JFK, ATL)
Fly(P3, SFO, ATL)
Fly(P2, ATL, SFO)
Fly(P3, ATL, JFK)
Load(C3, P3, JFK)
Fly(P3, JFK, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, SFO)
Fly(P2, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P2, JFK, SFO)
Fly(P1, ATL, JFK)
Unload(C3, P3, SFO)
Fly(P1, JFK, SFO)
Fly(P3, SFO, ATL)
Fly(P2, SFO, ATL)
Fly(P3, ATL, JFK)
Fly(P2, ATL, JFK)
Fly(P1, SFO, ATL)
Fly(P3, JFK, ATL)
Fly(P1, ATL, JFK)
Load(C2, P3, ATL)
Fly(P3, ATL, JFK)
Fly(P2, JFK, ATL)
Fly(P1, JFK, ATL)
Fly(P2, ATL, SFO)
Fly(P1, ATL, SFO)
Fly(P3, JFK, SFO)
Fly(P2, SFO, ATL)
Unload(C2, P3, SFO)
```

UCS
```
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Load(C3, P3, ATL)
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Fly(P3, ATL, SFO)
Unload(C3, P3, SFO)
Unload(C2, P2, SFO)
Unload(C1, P1, JFK)
```

### Optimal Solutions for problem 3:

BFS

```
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P1, SFO, ATL)
Load(C3, P1, ATL)
Fly(P2, JFK, ORD)
Load(C4, P2, ORD)
Fly(P1, ATL, JFK)
Unload(C1, P1, JFK)
Unload(C3, P1, JFK)
Fly(P2, ORD, SFO)
Unload(C2, P2, SFO)
Unload(C4, P2, SFO)
```
