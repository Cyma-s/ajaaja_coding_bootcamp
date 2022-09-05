import sys
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        result[a] += result[b]


input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    f = int(input().strip())
    parent = dict()
    result = dict()
    relation = []
    for i in range(f):
        a, b = input().strip().split()
        relation.append((a, b))
        if a not in parent:
            parent[a] = a
            result[a] = 1
        if b not in parent:
            parent[b] = b
            result[b] = 1
        union(a, b)
        print(result[find(a)])
