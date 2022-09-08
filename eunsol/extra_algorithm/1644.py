import math
import sys

input = sys.stdin.readline
n = int(input().strip())
prime = [True] * (n+1)
for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i]:
        j = 2
        while i * j <= n:
            prime[i * j] = False
            j += 1
prime_list = [i for i in range(2, n+1) if prime[i]]
end = 0
interval_sum = 0
count = 0
for start in range(len(prime_list)):
    while interval_sum < n and end < len(prime_list):
        interval_sum += prime_list[end]
        end += 1
    if interval_sum == n:
        count += 1
    interval_sum -= prime_list[start]
print(count)