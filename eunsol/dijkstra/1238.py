import heapq
import sys


def dijkstra(index, dest):
    heap = []
    dist = [sys.maxsize] * (n+1)
    heapq.heappush(heap, (0, index))
    dist[index] = 0
    while heap:
        time, town = heapq.heappop(heap)
        if dist[town] < time:
            continue
        for number, d in graph[town]:
            if dist[number] > time + d:
                dist[number] = time + d
                heapq.heappush(heap, (time + d, number))
    return dist[dest]


input = sys.stdin.readline
n, m, x = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
result = 0
for _ in range(m):
    a, b, t = map(int, input().strip().split())
    graph[a].append((b, t))
for i in range(1, n+1):
    start = dijkstra(i, x)
    end = dijkstra(x, i)
    result = max(result, start + end)
print(result)