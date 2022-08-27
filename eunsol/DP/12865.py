import sys
input = sys.stdin.readline
n, k = map(int, input().split())
weight = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(k + 1):
        if weight[i][0] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i][0]] + weight[i][1])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])
