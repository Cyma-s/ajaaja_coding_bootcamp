import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while queue:
        x, y, cnt, keys = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#' and visited[nx][ny][keys] == 0:
                if graph[nx][ny] == '.':
                    visited[nx][ny][keys] = 1
                    queue.append((nx, ny, cnt + 1, keys))
                elif graph[nx][ny] == '1':
                    return cnt + 1
                elif graph[nx][ny].islower():
                    new_keys = keys | (1 << (ord(graph[nx][ny]) - 97))
                    if visited[nx][ny][new_keys] == 0:
                        visited[nx][ny][keys] = 1
                        queue.append((nx, ny, cnt + 1, new_keys))
                elif graph[nx][ny].isupper():
                    if keys & 1 << (ord(graph[nx][ny]) - 65):
                        visited[nx][ny][keys] = 1
                        queue.append((nx, ny, cnt + 1, keys))
    return -1


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            queue.append((i, j, 0, 0))
            graph[i][j] = '.'
            visited[i][j][0] = 1
print(bfs())
