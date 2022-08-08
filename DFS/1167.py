import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a = list(map(int, input().split()))
    i=1
    while a[i]!=-1:
        graph[a[0]].append([a[i],a[i+1]])
        i+=2

def dfs(x, wei):
    for i in graph[x]:
        d,e = i
        if dis[d]==-1:
            dis[d] = wei+e
            dfs(d,wei+e)

dis = [-1]*(n+1)
dis[1]=0
dfs(1,0)

point = dis.index(max(dis))
dis = [-1]*(n+1)
dis[point]=0
dfs(point, 0)

print(max(dis))
