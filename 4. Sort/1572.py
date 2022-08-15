import sys

def update(index, val):
    while index <= 65539:
        tree[index] += val
        index += index & (-index)

def findmid():
    start = 1;
    end = 65536
    while start <= end:
        mid = (start + end) // 2
        num = 0
        index = mid
        while index > 0:
            num += tree[index]
            index -= index & (-index)

        if num < (K + 1) // 2:
            start = mid + 1
        else:
            end = mid - 1
    return end


N, K = map(int, input().split())
tree = [0] * 65540
lst = [int(sys.stdin.readline()) for _ in range(N)]

answer = 0
for n in range(N):
    update(lst[n] + 1, 1)

    if n > K - 1:
        update(lst[n - K] + 1, -1)
    if n >= K - 1:
        answer += findmid()

print(answer)
