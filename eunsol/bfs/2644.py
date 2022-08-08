from collections import deque


def bfs(x):
    queue = deque([x])
    while queue:
        number = queue.popleft()
        for node in graph[number]:
            if visited[node] == 0:
                visited[node] = visited[number] + 1
                queue.append(node)


n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
bfs(a)
if visited[b] > 0:
    print(visited[b])
else:
    print(-1)
