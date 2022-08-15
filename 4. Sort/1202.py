import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
jewel = []
for i in range(n):
    weight, price = map(int, input().rstrip().split())
    heapq.heappush(jewel, [weight, price])
bags = [int(input()) for _ in range(k)]
bags.sort()

answer = 0
tmp = []
for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewel)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not jewel:
        break
print(answer)