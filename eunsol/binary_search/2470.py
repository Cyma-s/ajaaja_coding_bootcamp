import sys

input = sys.stdin.readline
n = int(input())
value = list(map(int, input().split()))
value.sort()
left, right = 0, n-1
answer = value[left] + value[right]
start, end = left, right
while left < right:
    temp = value[left] + value[right]
    if abs(temp) < abs(answer):
        answer = temp
        start = left
        end = right
        if answer == 0:
            break
    if temp < 0:
        left += 1
    else:
        right -= 1
print(value[start], value[end])