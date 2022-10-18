import sys

input = sys.stdin.readline
n, s = map(int, input().strip().split())
_list = list(map(int, input().strip().split()))
sum_list = [0] * (n+1)
for i in range(1, n+1):
    sum_list[i] = sum_list[i-1] + _list[i-1]
count = sys.maxsize
end = 0
interval_sum = 0
interval_length = 0
for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += _list[end]
        interval_length += 1
        end += 1
    if interval_sum >= s:
        count = min(count, interval_length)
    interval_length -= 1
    interval_sum -= _list[start]
print(count if count != sys.maxsize else 0)