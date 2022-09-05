import sys
import heapq
INF = sys.maxsize
input=sys.stdin.readline
n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,t =map(int,input().split())
    graph[a].append((t,b))
    graph[b].append((t,a))
queue = []
dist = [[INF for _ in range(k+1)] for _ in range(n+1)]
def dijkstra(start):
    cnt = 0
    dist[start][cnt] = 0
    heapq.heappush(queue,(0,start,cnt))
    while queue:
        w,cur,cnt = heapq.heappop(queue)
        if dist[cur][cnt] < w:
            continue
        for time,next in graph[cur]:
            nextw =w+time
            if dist[next][cnt] > nextw:
                dist[next][cnt] = nextw
                heapq.heappush(queue,(nextw,next,cnt))
            if cnt<k and dist[next][cnt+1] >w:
                dist[next][cnt+1] = w
                heapq.heappush(queue,(w,next,cnt+1))
dijkstra(1)
print(min(dist[n]))