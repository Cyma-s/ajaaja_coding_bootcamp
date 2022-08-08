from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
a = ""
visited = dict()
for _ in range(3):
    temp = input().strip()
    temp = temp.replace(" ", "")
    a += temp
a = a.replace("0", "9")

def bfs():
    q = deque()
    q.append(a)
    visited[a] = 0
    while q:
        d = q.popleft()
        if d == 123456789:
            return visited[d]
        s = str(d)
        index = s.find('9')
        tx = index // 3
        ty = index % 3
        for i in range(4):
            x = dx[i] + tx
            y = dy[i] + ty
            if 0 <= x < 3 and 0 <= y < 3:
                target = x*3 + y
                ts = list(s)
                ts[index], ts[target] = ts[target], ts[index]
                ti = int(''.join(ts))
                if not visited.get(ti):
                    visited[ti] = visited[d] + 1
                    q.append(ti)
    return -1
print(bfs())