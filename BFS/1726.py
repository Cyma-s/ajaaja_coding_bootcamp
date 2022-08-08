from collections import deque
import sys

def bfs():
    q = deque()
    q.append((sX - 1, sY - 1, sD, 0))
    visit = [[[0 for _ in range(5)] for _ in range(n)] for _ in range(m)]
    visit[sX - 1][sY - 1][sD] = 1
    while q:
        x, y, d, cnt = q.popleft()
        if x == eX - 1 and y == eY - 1 and d == eD: return cnt
        nx, ny = x, y
        for i in range(3):
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny][d] == 1:
                continue
            if 0 <= nx < m and 0 <= ny < n and s[nx][ny] != 1:
                visit[nx][ny][d] = 1
                q.append([nx, ny, d, cnt + 1])
            else:
                break
        for i in range(1, 5):
            if d != i and visit[x][y][i] == 0:
                visit[x][y][i] = 1
                if (d == 1 and i == 2) or (d == 2 and i == 1) or (d == 3 and i == 4) or (d == 4 and i == 3):
                    q.append((x, y, i, cnt + 2))
                else:
                    q.append((x, y, i, cnt + 1))

input = sys.stdin.readline
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
sX, sY, sD = map(int, input().split())
eX, eY, eD = map(int, input().split())
print(bfs())
