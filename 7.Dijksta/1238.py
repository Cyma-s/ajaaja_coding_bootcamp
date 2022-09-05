import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline
n,m,x =map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int,input().split())
    graph[s].append((e,t))
def dijkstra(start):
    dist = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue,(0,start))
    dist[start] = 0
    while(queue):
        d, cur = heapq.heappop(queue)
        for node, weight in graph[cur]:
            if d + weight < dist[node]:
                dist[node] = d + weight
                heapq.heappush(queue, (d + weight, node))
    return dist
result = 0
for i in range(1,n+1):
    result = max(result,dijkstra(x)[i]+dijkstra(i)[x])
print(result)