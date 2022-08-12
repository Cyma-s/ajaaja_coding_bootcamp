import sys
from collections import deque


def dfs(graph, root) -> list:
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += reversed(graph[n])
    return visited


def bfs(graph, v):
    visited = []
    queue = deque([v])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n]
    return visited


n, m, v = map(int, sys.stdin.readline().split())
edges = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    e1, e2 = map(int, sys.stdin.readline().split())
    edges[e1].append(e2)
    edges[e2].append(e1)
for key in edges:
    edges[key].sort()

print(' '.join(list(map(str, dfs(edges, v)))))
print(' '.join(list(map(str, bfs(edges, v)))))
