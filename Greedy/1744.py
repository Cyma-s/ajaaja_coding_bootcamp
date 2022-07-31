n = int(input())
number = sorted([int(input()) for _ in range(n)], reverse=True)
minus, plus, zero_count = list(), list(), 0
for i in range(n):
    if number[i] > 0:
        plus.append(number[i])
    elif number[i] == 0:
        zero_count += 1
    else:
        minus.append(number[i])
minus.sort()
result = 0
while len(plus) > 1:
    if plus[0] == 1 or plus[1] == 1:
        result += (plus[0] + plus[1])
    else:
        result += (plus[0] * plus[1])
    del plus[:2]
while len(minus) > 1:
    result += (minus[0] * minus[1])
    del minus[:2]
if zero_count >= 1:
    minus.clear()
if plus:
    result += plus[0]
if minus:
    result += minus[0]
print(result)
