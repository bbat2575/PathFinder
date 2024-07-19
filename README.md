# PathFinder

**Uses breadth first search algorithm to check if a path exists between two vertices.**

Given a .in file representing an undirected graph, check if a path exists between a pair of vertices (called 'queries').

A .in file contains graph information in the following order:
1. Number of vertices
1. Number of edges
1. Edges - Starting vertex, ending vertex, and edge weight (edge weight is ignored!)
1. Number of queries
1. Queries

## Example

*graph8.in*

8           <- Number of vertices
7           <- Number of edges
0 1 0.802   <- Egdes
0 5 0.937   ...
0 7 0.019   ...
1 5 0.233   ...
2 3 0.154   ...
3 4 0.651   ...
6 7 0.010   ...
8           <- Number of queries
2 3         <- Queries
5 2         ...
2 1         ...
2 4         ...
7 0         ...
7 1         ...
1 4         ...
5 7         ...

Hence, graph8.in represents the following graph:

![alt text](https://github.com/bbat2575/PathFinder/blob/main/graph8.png)

## How To Run

How To Use:

```bash
./run.sh
```

NOTE: Ensure execution privileges are available.

```bash
chmod +x run.sh
```

## How To Run Tests

Simply execute the testing script.

```bash
./test.sh
```

NOTE: Ensure execution privileges are available.

```bash
chmod +x test.sh
```