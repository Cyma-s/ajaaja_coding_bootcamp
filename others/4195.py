import sys
input = sys.stdin.readline

def find(x):
    if x== parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a,b):
    a,b = find(a),find(b)
    if a==b:
        return
    else:
        parent[b]= a
        visited[a] += visited[b]

t= int(input())
for _ in range(t):
    f= int(input())
    parent = dict()
    visited = dict()
    for i in range(f):
        a,b = map(str, input().split())
        if a not in parent:
            parent[a] =a
            visited[a]=1
        if b not in parent:
            parent[b] =b
            visited[b]=1

        union(a,b)
        print(visited[find(a)])
