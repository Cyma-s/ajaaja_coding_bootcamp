import heapq
n = int(input())
pq = [int(input()) for _ in range(n)]
heapq.heapify(pq)
count = 0
while len(pq) > 1:
    a, b = heapq.heappop(pq), heapq.heappop(pq)
    count += (a+b)
    heapq.heappush(pq, a+b)
print(count)