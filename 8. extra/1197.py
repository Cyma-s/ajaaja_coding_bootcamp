import sys
input = sys.stdin.readline
v,e = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(e)]
graph.sort(key=lambda x:x[0])
parent = list(range(v+1))
def union(i,j):
    i = find(i)
    j = find(j)
    if i<j:
        parent[j]=i
    else:
        parent[i]=j
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

result=0
for w,s,e in graph:
    if find(s)!=find(e):
        union(s,e)
        result+=w
print(result)