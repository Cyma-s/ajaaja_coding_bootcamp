import sys
def find(x):
    if parent[x] == x:
        return parent[x]
    return find(parent[x])

def union_parent(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    graph = []
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    for i in range(n):
        x, y, r = map(int, input().strip().split())
        graph.append((x, y, r))
    for i in range(n):
        for j in range(i+1, n):
            x_dist = graph[i][0] - graph[j][0]
            y_dist = graph[i][1] - graph[j][1]
            r_dist = graph[i][2] + graph[j][2]
            if x_dist ** 2 + y_dist ** 2 <= r_dist ** 2:
                union_parent(i, j)
    result = len([i for i in range(n) if i == parent[i]])
    print(result)
