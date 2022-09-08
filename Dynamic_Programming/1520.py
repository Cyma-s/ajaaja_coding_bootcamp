import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
dx = [1,-1,0,0]
dy = [0,0,-1,1]
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
check = [[-1] * n for _ in range(m)]

def dfs(x,y):
    if x==m-1 and y == n-1:
        return 1
    if check[x][y] != -1:
        return check[x][y]

    cnt = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n and board[x][y]>board[nx][ny]:
            cnt += dfs(nx,ny)

    check[x][y]=cnt
    return check[x][y]

print(dfs(0,0))

