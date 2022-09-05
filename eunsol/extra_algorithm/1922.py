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
n = int(input().strip())
m = int(input().strip())
costs = []
parent = [0] * (n + 1)
result = 0
for i in range(1, n+1):
    parent[i] = i
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    costs.append((c, a, b))
costs.sort()
for cost in costs:
    length, a, b = cost
    if find(a) != find(b):
        union(a, b)
        result += length
print(result)
