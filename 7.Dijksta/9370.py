import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, arr):
    q = []
    heapq.heappush(q, (0, start))
    visited = [sys.maxsize for _ in range(n+1)]
    visited[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if visited[node] < dist:
            continue
        for ndist, nnode in arr[node]:
            if visited[nnode] > dist+ndist:
                visited[nnode] = dist+ndist
                heapq.heappush(q, (dist+ndist, nnode))
    return visited


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    start, x, y = map(int, input().split())
    arr = [[]for _ in range(n+1)]
    for _ in range(m):
        a, b, dist = map(int, input().split())
        arr[a].append((dist, b))
        arr[b].append((dist, a))
    goal = []
    for _ in range(t):
        goal.append(int(input()))

    s = dijkstra(start, arr)
    m1 = dijkstra(x, arr)
    m2 = dijkstra(y, arr)
    result = []
    for k in goal:
        if s[x]+m1[y]+m2[k] == s[k] or s[y]+m2[x]+m1[k] == s[k]:
            result.append(k)
    print(*sorted(result))