import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
def dfs(x, y):
    if y == c-1:
        return True
    for i in range(3):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and graph[nx][ny] == '.':
            visited[nx][ny] = 1
            if dfs(nx, ny):
                return True
    return False


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx = [-1, 0, 1]
dy = [1, 1, 1]
visited = [[0] * c for _ in range(r)]
result = 0
for i in range(r):
    if graph[i][0] == '.':
        visited[i][0] = 1
        if dfs(i, 0):
            result += 1
print(result)
