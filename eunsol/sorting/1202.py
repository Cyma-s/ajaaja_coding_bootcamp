import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
jewels = sorted([list(map(int, input().split())) for _ in range(n)])
bag_weight = sorted([int(input()) for _ in range(k)])
heap = []
total = 0
for bag in bag_weight:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(heap, -jewels[0][1])
        heapq.heappop(jewels)
    if heap:
        total += heapq.heappop(heap)
    elif not jewels:
        break
print(-total)