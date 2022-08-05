import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(x,y):
    dmax =0
    global result
    for z in graph[x]:
        if z != y:
            dmax = max(dmax,dfs(z,x))
    if dmax >= d:
        result +=1
    return dmax+1
n,s,d = map(int,input().split())
graph = {i: [] for i in range(1,n+1)}
visited = [0]*(n+1)
result = 0
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

dfs(s,0)
if result<1:
    print(0)
else:
    print(2*(result-1))