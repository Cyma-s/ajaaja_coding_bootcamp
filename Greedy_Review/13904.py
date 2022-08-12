import sys
input = sys.stdin.readline
n = int(input())
task = []
ans = [0 for _ in range(1000)]

for i in range(n):
    a,b = map(int, input().split())
    task.append([a,b])

task.sort(reverse = True, key=lambda x: x[1])
for i in range(n):
    for j in range(task[i][0]-1, -1,-1):
        if ans[j]==0:
            ans[j] = task[i][1]
            break

print(sum(ans))
