import sys
input = sys.stdin.readline
INF =sys.maxsize
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[INF]* (1<<n) for _ in range(n)]
def dfs(cur,visited):
    if visited == (1<<n)-1:
        if matrix[cur][0] ==0:
            return INF
        else:
            return matrix[cur][0]
    if dp[cur][visited]!=INF:
        return dp[cur][visited]
    for i in range(1,n):
        if not visited & (1<<i) and matrix[cur][i] !=0:
            dp[cur][visited] = min(dp[cur][visited],dfs(i,visited|(1<<i))+matrix[cur][i])
    return dp[cur][visited]
print(dfs(0,1))