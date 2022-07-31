n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
for i in range(len(time)):
    time[i].reverse()
time.sort()
end_time, count = 0, 0
for end, start in time:
    if end_time <= start:
        end_time = end
        count += 1
print(count)
