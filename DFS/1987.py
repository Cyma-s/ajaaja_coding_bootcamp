import sys
n, m = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visit = [0]*26
max = 0
def dfs(x,y,cnt):
    global max
    if max < cnt:
        max = cnt

    for i in range(4):
        x2 = x+dx[i]
        y2 = y+dy[i]
        if 0<=x2<n and 0<=y2<m and visit[board[x2][y2]]==0:
            visit[board[x2][y2]]=1
            cnt2 = cnt+1
            dfs(x2,y2,cnt2)
            visit[board[x2][y2]]=0

visit[board[0][0]]=1
dfs(0,0,1)
print(max)
