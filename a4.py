from collections import deque

# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

edges, queries = [], []

for _ in range(m):
    edges.append(input().split())

q = int(input())

for _ in range(q):
    queries.append(input().split())
	
# Print a `1` to stdout for each query. This section should be altered to instead print a `1` where the
# query indicates a connection and `0` else.

# Create and adjacency list
adj_list = {}

# Populate adjacency list
for e in edges:
    if e[0] in adj_list:
        adj_list[e[0]].add(e[1])
    else:
        adj_list[e[0]] = set([e[1]])

    if e[1] in adj_list:
        adj_list[e[1]].add(e[0])
    else:
        adj_list[e[1]] = set([e[0]])

# Iterate over queries and check for a path
for _ in queries:
    # Initialise a list to keep track of visited vertices
    visited = [False for i in range(n)]
    # Create a list that stores adjacent vertices to be checked and add starting vertex
    current = [int(_[0])]
    visited[current[0]] = True

    # While current is not empty, check next vertex
    while current:
        vertex = current.pop(0)
        # Retrieve adjacent vertices that have not been visited and store in current
        try:
            for i in adj_list[str(vertex)]:
                if not visited[int(i)]:
                    current.append(int(i))
                    visited[int(i)] = True
        except:
            pass

    # Check if a path exists
    if visited[int(_[0])] and visited[int(_[1])]:
        print(f"{_[0]}, {_[1]} -> Path Exists!")
    else:
        print(f"{_[0]}, {_[1]} -> No Path Exists.")

