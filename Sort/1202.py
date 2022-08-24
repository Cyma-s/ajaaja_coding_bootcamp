import heapq
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
jewelry = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
jewelry.sort()
bag.sort()
result = 0
tmp = []
for i in bag:
    while jewelry and i >= jewelry[0][0]:
        heapq.heappush(tmp, -jewelry[0][1])
        heapq.heappop(jewelry)
    if tmp:
        result+=heapq.heappop(tmp)
    elif not jewelry:
        break

print(-result)
