import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for  _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
def bfs(s):
    cnt = 1
    q = deque([s])
    visited = [0] * (n+1)
    visited[s] = 1
    while q:
        for x1 in graph[q.popleft()]:
            if not visited[x1]:
                visited[x1] = 1
                cnt += 1
                q.append(x1)
    return cnt
result = []
cmax =0
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt == cmax:
        result.append(i)
    if cmax < cnt:
        cmax = cnt
        result = []
        result.append(i)
print(*result)
