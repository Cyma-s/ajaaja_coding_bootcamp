import sys
input = sys.stdin.readline
n, c = map(int, input().split())
coord = [int(input()) for _ in range(n)]
coord.sort()
left, right = 1, coord[-1] - coord[0]
answer = coord[1] - coord[0]
while left <= right:
    mid = (left + right) // 2
    count, prev = 1, coord[0]
    for i in range(n):
        if coord[i] - prev >= mid:
            count += 1
            prev = coord[i]
    if count < c:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1
print(answer)