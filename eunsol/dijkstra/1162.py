import heapq
import sys
def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 1, 0))  # 시간, 도시, 포장 횟수
    dist[0][0] = 0
    while heap:
        time, city, count = heapq.heappop(heap)
        if dist[city][count] < time:
            continue
        for other, other_time in graph[city]:
            if dist[other][count] > time + other_time:
                dist[other][count] = time + other_time
                heapq.heappush(heap, (time + other_time, other, count))
            if count < k and dist[other][count + 1] > time:
                dist[other][count + 1] = time
                heapq.heappush(heap, (time, other, count+1))


input = sys.stdin.readline
n, m, k = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
dist = [[sys.maxsize] * (k+1) for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().strip().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
dijkstra()
print(min(dist[n]))