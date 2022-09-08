import sys
import heapq
input = sys.stdin.readline
INF = 100000000

v,e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    x ,y, z = map(int, input().split())
    graph[x].append((y,z))

dist = [INF]*(v+1)

q = []
def dijkstra(a):
    dist[a] = 0
    heapq.heappush(q,(0,a))
    while q:
        dis, now = heapq.heappop(q)
        for n, wei in graph[now]:
            cost = dis + wei
            if cost < dist[n]:
                dist[n] = cost
                heapq.heappush(q,(cost,n))

dijkstra(k)
for i in dist[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")
