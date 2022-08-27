import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
dx = [1,-1,0,0]
dy = [0,0,-1,1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
cnt = 0
def dfs(x,y):
    if check[x][y]:
        return check[x][y]
    check[x][y]=1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and board[x][y]<board[nx][ny]:
            check[x][y] = max(check[x][y], dfs(nx,ny)+1)
    return check[x][y]

for i in range(n):
    for j in range(n):
        cnt = max(cnt,dfs(i,j))
print(cnt)

