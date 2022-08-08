from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        node = q.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                visited[n] = visited[node] + 1
                q.append(n)

n = int(input())
graph = [[] for _ in range(n + 1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n + 1)
bfs(s)
if visited[e]>0:
    print(visited[e])
else:
    print(-1)
