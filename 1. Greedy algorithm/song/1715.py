import heapq
card = []
for _ in range(int(input())):
    heapq.heappush(card, int(input()))
result = 0
if len(card) <=1:
    print(0)
    exit(1)
while len(card) > 1:
    add = heapq.heappop(card) + heapq.heappop(card)
    result += add
    heapq.heappush(card,add)
print(result)