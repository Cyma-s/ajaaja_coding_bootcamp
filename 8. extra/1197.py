import sys
input = sys.stdin.readline
v,e = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(e)]
graph.sort(key=lambda x:x[2])
parent = list(range(v+1))
def union(i,j):
    i = find(i)
    j = find(j)
    if j<i:
        parent[i]=j
    else:
        parent[j]=i
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

result=0
for w,s,e in graph:
    if find(w)!=find(s):
        union(w,s)
        result+=e
print(result)