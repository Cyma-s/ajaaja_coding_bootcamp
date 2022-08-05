import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
pn = int(input())
graph = [[] for _ in range(n+1)]
for i in range(pn):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] *(n+1)
def dfs(i):
    visited[i] = 1
    for a in graph[i]:
        if visited[a] == 0:
            dfs(a)
dfs(1)
print(sum(visited)-1)