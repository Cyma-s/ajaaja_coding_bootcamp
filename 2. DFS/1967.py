import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x,w):
    for i,j in graph[x]:
        if visited[i] == -1:
            visited[i] = w + j
            dfs(i, w+j)
n=int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [-1] *(n+1)
visited[1] = 0
dfs(1,0)

start = visited.index(max(visited))

visited = [-1] *(n+1)
visited[start] = 0
dfs(start,0)
print(max(visited))