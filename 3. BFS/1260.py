import sys
from collections import deque
input=sys.stdin.readline

n,m,v=map(int,input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited=[0]*(n+1)
visited1=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b] = graph[b][a] =1

def bfs(v):
  q = deque()
  q.append(v)
  visited[v] = 1
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, n + 1):
      if visited[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visited[i] = 1

def dfs(v):
  visited1[v] = 1
  print(v, end = " ")
  for i in range(1, n + 1):
    if visited1[i] == 0 and graph[v][i] == 1:
      dfs(i)

dfs(v)
print()
bfs(v)
