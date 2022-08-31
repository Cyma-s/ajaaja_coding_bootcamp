import sys
import heapq
input =sys.stdin.readline
INF = sys.maxsize
v,e = map(int,input().split())
k=int(input())
graph = [[] for _ in range(v+1)]
queue = []
dist = [INF] *(v+1)
for i in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
def dijksta(k):
    dist[k] = 0
    heapq.heappush(queue,(0,k))
    while queue:
        d,cur = heapq.heappop(queue)
        for node,weight in graph[cur]:
            if d+weight < dist[node]:
                dist[node] = d+weight
                heapq.heappush(queue,(d+weight,node))
dijksta(k)
for i in dist[1:]:
    if i==INF:
        print('INF')
    else:
        print(i)