import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

def bfs(point):
    d=0
    q= deque()
    q.append(point)
    visit = [0]*(n+1)
    visit[point]=1
    while q:
        c= q.popleft()
        d+=1
        for i in graph[c]:
            if not visit[i]:
                visit[i]=1
                q.append(i)
    return d

max =0
result =[]
for i in range(1, n+1):
    if graph[i]:
        value = bfs(i)
        if max <= value:
            if max < value:
                result = []
            max = value
            result.append(i)

print(*result)
