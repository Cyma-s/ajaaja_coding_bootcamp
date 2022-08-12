import sys


def solve():
    global result, weight
    while len(weight) > 0:
        for i in range(len(crane)):
            for j in range(len(weight)):
                if crane[i] >= weight[j]:
                    weight.pop(j)
                    break
        result += 1


input = sys.stdin.readline
n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
weight = sorted(list(map(int, input().split())), reverse=True)
result = 0
if crane[0] < weight[0]:
    print(-1)
else:
    solve()
    print(result)
