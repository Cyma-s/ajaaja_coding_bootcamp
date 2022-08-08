from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y,0])
    visit[x][y][0]=1
    while q:
        x,y,z = q.popleft()
        if board[x][y]=='1':
            print(visit[x][y][z]-1)
            return
        for i in range(4):
            x2 = x+dx[i]
            y2 = y+dy[i]
            if 0 <= x2 < n and 0 <= y2 < m:
                if board[x2][y2] != '#' and visit[x2][y2][z] == 0:
                    if board[x2][y2].islower():
                        z2 = z | (1 << (ord(board[x2][y2]) - ord('a')))
                        if visit[x2][y2][z2] == 0:
                            visit[x2][y2][z2] = visit[x][y][z] + 1
                            q.append([x2, y2, z2])
                    elif board[x2][y2].isupper():
                        if z & (1 << (ord(board[x2][y2]) - ord('A'))):
                            visit[x2][y2][z] = visit[x][y][z] + 1
                            q.append([x2, y2, z])
                    else:
                        visit[x2][y2][z] = visit[x][y][z] + 1
                        q.append([x2, y2, z])
    print(-1)

input= sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visit = [[[0]*64 for _ in range(m)] for _ in range(n)]
for i in range(n):
        for j in range(m):
            if board[i][j] == '0':
                bfs(i,j)

