import sys
import heapq
input = sys.stdin.readline
INF = 100000000

n,m,e = map(int, input().split())
s = [[] for _ in range(n+1)]
dist = [INF]*(n+1)
s_r = [[] for _ in range(n+1)]
dist_r = [INF]*(n+1)
q=[]


def dijkstra(a, dist, s):
    dist[a] = 0
    heapq.heappush(q, [0, a])
    while q:
        dis, now = heapq.heappop(q)
        if dist[now]<dis:
            continue
        for n2, wei in s[now]:
            cost = dis + wei
            if cost < dist[n2]:
                dist[n2] = cost
                heapq.heappush(q,[cost,n2])

for _ in range(m):
    x ,y, z = map(int, input().split())
    s[x].append([y,z])
    s_r[y].append([x,z])

dijkstra(e,dist,s)
dijkstra(e,dist_r,s_r)
max2 = 0
for i in range(1,n+1):
    max2 = max(max2, dist[i]+dist_r[i])
print(max2)
