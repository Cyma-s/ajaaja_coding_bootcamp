import sys
from collections import deque

input = sys.stdin.readline
dir_dx = [0, 0, 0, 1, -1]
dir_dy = [0, 1, -1, 0, 0]


def bfs():
    while queue:
        x, y, dir, cnt = queue.popleft()
        if x == end_x - 1 and y == end_y - 1 and dir == end_dir:
            return cnt
        for i in range(1, 4):
            nx = x + dir_dx[dir] * i
            ny = y + dir_dy[dir] * i
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny][dir] == 1: continue
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] != 1:
                visited[nx][ny][dir] = 1
                queue.append((nx, ny, dir, cnt + 1))
            else:
                break
        for i in range(1, 5):
            if dir != i and visited[x][y][i] == 0:
                visited[x][y][i] = 1
                if (dir == 1 and i == 2) or (dir == 2 and i == 1) or (dir == 3 and i == 4) or (dir == 4 and i == 3):
                    queue.append((x, y, i, cnt + 2))
                else:
                    queue.append((x, y, i, cnt + 1))


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
start_x, start_y, start_dir = map(int, input().split())
end_x, end_y, end_dir = map(int, input().split())
queue = deque()
queue.append([start_x - 1, start_y - 1, start_dir, 0])
visited = [[[0] * 5 for _ in range(n)] for _ in range(m)]
visited[start_x - 1][start_y-1][start_dir] = 1
print(bfs())