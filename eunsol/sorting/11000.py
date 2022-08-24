import heapq
import sys
n = int(input())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time.sort()
end_time = []
heapq.heappush(end_time, 0)
for i in range(n):
    if time[i][0] >= end_time[0]:
        heapq.heappop(end_time)
        heapq.heappush(end_time, time[i][1])
    else:
        heapq.heappush(end_time, time[i][1])

print(len(end_time))