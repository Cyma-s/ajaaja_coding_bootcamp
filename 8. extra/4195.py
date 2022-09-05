import sys
input = sys.stdin.readline
def union(i,j):
    i = find(i)
    j = find(j)
    if i!=j:
        parent[j]=i
        visited[i]+=visited[j]
    print(visited[i])
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]
t = int(input())

for _ in range(t):
    f = int(input())
    parent = dict()
    visited = dict()
    for _ in range(f):
        a,b= input().split()
        if a not in parent:
            parent[a] =a
            visited[a]=1
        if b not in parent:
            parent[b] =b
            visited[b] =1
        union(a,b)
