from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
c = [[[0]*64 for _ in range(m)] for _ in range(n)]
q = deque()

def bfs(x, y):
    q.append([x, y, 0])
    c[x][y][0] = 1
    while q:
        x, y, z = q.popleft()
        if a[x][y] == '1':
            print(c[x][y][z] - 1)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] != '#' and c[nx][ny][z] == 0:
                    if a[nx][ny].islower():
                        nz = z | (1 << (ord(a[nx][ny]) - ord('a')))
                        if c[nx][ny][nz] == 0:
                            c[nx][ny][nz] = c[x][y][z] + 1
                            q.append([nx, ny, nz])
                    elif a[nx][ny].isupper():
                        if z & (1 << (ord(a[nx][ny]) - ord('A'))):
                            c[nx][ny][z] = c[x][y][z] + 1
                            q.append([nx, ny, z])
                    else:
                        c[nx][ny][z] = c[x][y][z] + 1
                        q.append([nx, ny, z])
    print(-1)
for i in range(n):
    for j in range(m):
        if a[i][j] == '0':
            bfs(i, j)