import sys
input = sys.stdin.readline
n,k = map(int,input().split())
i = [list(map(int,input().split())) for _ in range(n)]
items=[[0,0]] + i[0:]
dp = [0 for _ in range(k+1)]
for item in items:
    for i in range(k,item[0]-1,-1):
        dp[i] = max(dp[i],dp[i-item[0]]+item[1])
print(dp[-1])