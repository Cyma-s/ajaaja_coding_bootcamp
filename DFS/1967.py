import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

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
