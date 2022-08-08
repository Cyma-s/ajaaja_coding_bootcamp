import sys
import collections
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, weight):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = weight + b
            dfs(a, weight+b)


v = int(input())
graph = collections.defaultdict(list)
visited = [-1] * (v+1)
for _ in range(v):
    ipt = list(map(int, input().split()))
    for i in range(1, len(ipt) - 1, 2):
        graph[ipt[0]].append((ipt[i], ipt[i+1]))
visited[1] = 0
dfs(1, 0)
start = visited.index(max(visited))
visited = [-1] * (v+1)
visited[start] = 0
dfs(start, 0)
print(max(visited))
