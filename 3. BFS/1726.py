from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())

def bfs():
    q = deque()
    q.append([sx - 1, sy - 1, sd, 0])
    visited = [[[0 for _ in range(5)] for _ in range(n)] for _ in range(m)]
    visited[sx - 1][sy - 1][sd] = 1
    while q:
        x, y, d, cnt = q.popleft()
        if x == ex - 1 and y == ey - 1 and d == ed: return cnt
        nx, ny = x, y
        for i in range(3):
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny][d] == 1: continue
            if 0 <= nx < m and 0 <= ny < n and s[nx][ny] != 1:
                visited[nx][ny][d] = 1
                q.append([nx, ny, d, cnt + 1])
            else: break
        for i in range(1, 5):
            if d != i and visited[x][y][i] == 0:
                visited[x][y][i] = 1
                if (d == 1 and i == 2) or (d == 2 and i == 1) or (d == 3 and i == 4) or (d == 4 and i == 3):
                    q.append([x, y, i, cnt + 2])
                else:
                    q.append([x, y, i, cnt + 1])
print(bfs())