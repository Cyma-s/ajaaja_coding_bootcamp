import sys
n = int(input())
m = int(input())
computers = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    computers[x].append(y)
    computers[y].append(x)
visited = []
stack = [1]
while stack:
    com = stack.pop()
    if com not in visited:
        visited.append(com)
        stack += computers[com]
print(len(visited)-1)