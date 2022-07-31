n = int(input())
money = list(map(int, input().split()))
money.sort()
time = 0
for i in range(n):
    for j in range(i+1):
        time += money[j]
print(time)
