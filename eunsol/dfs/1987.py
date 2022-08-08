import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(x, y, number):
    global result
    result = max(result, number)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if not visited_alphabet[ord(graph[nx][ny]) - 65] and not visited[nx][ny]:
            visited_alphabet[ord(graph[nx][ny]) - 65] = True
            visited[nx][ny] = True
            dfs(nx, ny, number + 1)
            visited_alphabet[ord(graph[nx][ny]) - 65] = False
            visited[nx][ny] = False


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
visited = [[False] * c for _ in range(r)]
visited[0][0] = True
visited_alphabet = [False] * 26
visited_alphabet[ord(graph[0][0]) - 65] = True
dfs(0, 0, 1)
print(result)
