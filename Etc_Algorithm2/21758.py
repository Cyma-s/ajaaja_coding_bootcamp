import sys
input = sys.stdin.readline
n = int(input())
honey = list(map(int, input().split()))
ans = 0
sum = []
sum.append(honey[0])
for i in range(1,n):
    sum.append(sum[i-1]+honey[i])

for i in range(1,n-1):
    ans = max(ans, sum[n-2]+sum[i-1]-honey[i])

for i in range(1,n-1):
    ans = max(ans, sum[n-1] - honey[0] - honey[i] + sum[n-1] - sum[i])

for i in range(1,n-1):
    ans = max(ans, sum[n-2] - honey[0] + honey[i])

print(ans)
