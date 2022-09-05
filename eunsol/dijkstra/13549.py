import sys
import heapq


def dijkstra():
    queue = []
    heapq.heappush(queue, (0, n))
    dist[n] = 0
    while queue:
        time, loc = heapq.heappop(queue)
        if time > dist[loc]:
            continue
        if 0 <= loc * 2 < 2 * length + 1 and dist[loc * 2] > time:
            dist[loc * 2] = time
            heapq.heappush(queue, (time, loc * 2))
        for i in (loc - 1, loc + 1):
            if 0 <= i < 2 * length + 1 and dist[i] > time + 1:
                dist[i] = time + 1
                heapq.heappush(queue, (time + 1, i))


input = sys.stdin.readline
n, k = map(int, input().strip().split())
length = max(n, k)
dist = [sys.maxsize] * (2 * length + 1)
dijkstra()
print(dist[k])
