import heapq
import sys
input = sys.stdin.readline
n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

if len(card)==1:
    print(0)
else:
    num = 0
    while len(card) > 1:
        temp1 = heapq.heappop(card)
        temp2 = heapq.heappop(card)
        num += temp1 + temp2
        heapq.heappush(card, temp1+temp2)
    print(num)
