import sys

input = sys.stdin.readline
n = int(input().strip())
solution = list(map(int, input().strip().split()))
solution.sort()
result = solution[-1] + solution[-2] + solution[-3]
result_solution = [solution[-1], solution[-2], solution[-3]]
for one in range(n-1):
    left, right = one + 1, n-1
    start, end = left, right
    while left < right:
        temp = solution[one] + solution[left] + solution[right]
        if abs(temp) < abs(result):
            result = temp
            result_solution = [solution[one], solution[left], solution[right]]
            start = left
            end = right
            if result == 0:
                break
        if temp < 0:
            left += 1
        else:
            right -= 1
result_solution.sort()
print(*result_solution)
