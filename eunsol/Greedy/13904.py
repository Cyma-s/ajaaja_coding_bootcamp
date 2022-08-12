import sys
input = sys.stdin.readline
n = int(input())
hw = sorted([list(map(int, input().split())) for _ in range(n)])
total_day = hw[-1][0]
total_score = 0
possible_day = []
while True:
    if total_day == 0:
        break
    while hw and hw[-1][0] >= total_day:
        possible_day.append(hw.pop())
    total_day -= 1
    if not possible_day:
        continue
    possible_day.sort(key=lambda x: x[1])
    total_score += possible_day.pop()[1]
print(total_score)
