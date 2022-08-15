import sys
import heapq
input = sys.stdin.readline
n = int(input())
road = []
for _ in range(n):
    road.append(list(map(int, input().split())))
d = int(input())
roads = []
for i in road:
    a,b = i
    if abs(b-a)<=d:
        i = sorted(i)
        roads.append(i)
roads.sort(key = lambda x:x[1])
cnt = 0
heap = []
for i in roads:
    if not heap:
        heapq.heappush(heap, i)
    else:
        while heap[0][0] < i[1]-d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap,i)
    cnt = max(cnt, len(heap))
print(cnt)
