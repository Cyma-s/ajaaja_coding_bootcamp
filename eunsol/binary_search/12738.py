def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


N = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in arr:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[binary_search(i, 0, len(dp)-1)] = i
print(len(dp))