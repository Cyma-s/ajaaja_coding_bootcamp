import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
result =0
forest = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
def dfs(x,y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < n and 0 <= y+dy < n:
                if forest[x+dx][y+dy] > forest[x][y]:
                    dp[x][y] =max(dp[x][y], dfs(x+dx, y+dy))
    return dp[x][y]+1
for i in range(n):
    for j in range(n):
        result = max(result,dfs(i,j))
print(result)