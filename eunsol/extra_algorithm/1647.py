import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
n, m = map(int, input().strip().split())
roads = []
parent = [0] * (n + 1)
result = []
max_value = 0
for i in range(1, n + 1):
    parent[i] = i
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    roads.append((c, a, b))
roads.sort()
for i in range(m):
    length, a, b = roads[i]
    if find(a) != find(b):
        union(a, b)
        result.append(length)
        max_value = max(max_value, length)
print(sum(result) - max_value)
