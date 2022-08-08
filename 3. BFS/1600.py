import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
w,h = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(h)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
hdx = [-2,-2,-1,-1,1,1,2,2]
hdy = [-1,1,-2,2,-2,2,-1,1]
def bfs():
    q = deque()
    q.append((0,0,k))
    visited = [[[0]*(31) for _ in range(w)] for _ in range(h)]
    while q:
        x,y,z = q.popleft()
        if x == h-1 and y == w-1:
            return visited[x][y][z]
        if z>0:
            for i in range(8):
                nx, ny = x+hdx[i], y+hdy[i]
                if 0<=nx<h and 0<=ny<w and visited[nx][ny][z-1] ==0 and board[nx][ny]==0:
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    q.append((nx,ny,z-1))
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<h and 0<=ny<w and visited[nx][ny][z] ==0 and board[nx][ny]==0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx,ny,z))

    return -1
print(bfs())
