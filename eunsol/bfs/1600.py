import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
queue = deque()
horse_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
horse_dy = [2, 1, -1, -2, -2, -1, 1, 2]
monkey_dx = [-1, 1, 0, 0]
monkey_dy = [0, 0, -1, 1]
visited = [[[sys.maxsize] * w for _ in range(h)] for _ in range(k+1)]
visited[0][0][0] = 0
queue.append((0, 0, 0))
while queue:
    z, x, y = queue.popleft()
    if z+1 <= k:
        for i in range(8):
            nx = horse_dx[i] + x
            ny = horse_dy[i] + y
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] == 1:
                continue
            if visited[z+1][nx][ny] > visited[z][x][y] + 1:
                visited[z + 1][nx][ny] = visited[z][x][y] + 1
                queue.append((z+1, nx, ny))
    for i in range(4):
        nx = monkey_dx[i] + x
        ny = monkey_dy[i] + y
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        if graph[nx][ny] == 1:
            continue
        if visited[z][nx][ny] > visited[z][x][y] + 1:
            visited[z][nx][ny] = visited[z][x][y] + 1
            queue.append((z, nx, ny))
result = min(visited[i][h-1][w-1] for i in range(k+1))
print(result if result != sys.maxsize else -1)