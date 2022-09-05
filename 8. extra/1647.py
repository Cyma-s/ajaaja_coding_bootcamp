import sys
input = sys.stdin.readline
n ,m= map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
graph.sort(key=lambda x:x[2])
parent = list(range(n+1))
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
    if find(w)!=find(s):
        union(w,s)
        result+=e
        last = e
print(result-last)