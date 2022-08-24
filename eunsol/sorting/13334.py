import heapq
n = int(input())
train_list = [sorted(list(map(int, input().split()))) for _ in range(n)]
train_list.sort(key = lambda x: (x[1], x[0]))
d = int(input())
heap = []
result = -1
for start, end in train_list:
    length = end-d
    if start >= length:
        heapq.heappush(heap, start)
    while heap and heap[0] < length:
        heapq.heappop(heap)
    result = max(result, len(heap))
print(result)
