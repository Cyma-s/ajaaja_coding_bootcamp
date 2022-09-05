import heapq
import sys
def dijkstra(start):
    heap = []
    dist = [sys.maxsize] * (n+1)
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    while heap:
        road, city = heapq.heappop(heap)
        if dist[city] < road:
            continue
        for next_city, distance in graph[city]:
            if dist[next_city] > distance + road:
                dist[next_city] = distance + road
                heapq.heappush(heap, (distance + road, next_city))
    return dist


input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    n, m, t = map(int, input().strip().split())
    s, g, h = map(int, input().strip().split())
    graph = [[] for _ in range(n+1)]
    end = []
    result = []
    for i in range(m):
        a, b, d = map(int, input().strip().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    for i in range(t):
        end.append(int(input().strip()))
    start_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)
    for length in end:
        if start_dist[g] + g_dist[h] + h_dist[length] == start_dist[length] \
            or start_dist[h] + h_dist[g] + g_dist[length] == start_dist[length]:
            result.append(length)
    result.sort()
    print(*result)
