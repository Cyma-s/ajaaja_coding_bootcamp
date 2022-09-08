import sys
input = sys.stdin.readline
v,e = map(int, input().split())
edge = []
for _ in range(e):
    a,b,c = map(int, input().split())
    edge.append((c,a,b))
edge.sort(key=lambda x: x[0])
parent = list(range(v + 1))

def union(a,b):
    a = find(a)
    b = find(b)
    if b<a:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

sum = 0
for a,b,c in edge:
    if find(b) != find(c):
        union(b, c)
        sum += a
print(sum)
