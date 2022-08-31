import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n,k = map(int,input().split())
queue = []
dist = [INF] * 100001
def dijkstra(start):
    dist[start] = 0
    heapq.heappush(queue,(0,start))
    while (queue):
        d, cur = heapq.heappop(queue)
        for i in [cur*2,cur+1,cur-1]:
            if 0<=i<=100000:
                if i == cur*2 and dist[i] == INF:
                    heapq.heappush(queue,(d,i))
                    dist[i] = d
                elif dist[i] ==INF:
                    heapq.heappush(queue,(d+1,i))
                    dist[i] = d+1
    return dist

if k<=n:
    print(n-k)
else:
    dijkstra(n)
    print(dist[k])