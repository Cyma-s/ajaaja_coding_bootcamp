from collections import deque
def bfs(a):
    q = deque()
    q.append(a)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visit[i] == 0:
                visit[i] = visit[a] + 1
                q.append(i)


n = int(input())
graph = [[] for _ in range(n + 1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visit = [0] * (n + 1)
bfs(s)
print(visit[e] if visit[e] > 0 else -1)
