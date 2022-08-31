import sys
input = sys.stdin.readline
m,n = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1] * (n) for _ in range(m)]

def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if map[x+dx][y+dy] < map[x][y]:
                    dp[x][y] += dfs(x+dx, y+dy)
    return dp[x][y]
print(dfs(0,0))