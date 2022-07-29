n = int(input())
num1 = []
nnum = []
pnum = []
result = 0
for _ in range(n):
    num = int(input())
    if num == 1:
        num1.append(num)
    elif num > 1:
        pnum.append(num)
    else:
        nnum.append(num)
pnum.sort(reverse=False)
nnum.sort(reverse=True)
while len(pnum) != 0:
    if len(pnum) == 1:
        result += pnum.pop()
    else:
        result += pnum.pop() * pnum.pop()
while len(nnum) != 0:
    if len(nnum) == 1:
        result += nnum.pop()
    else:
        result += nnum.pop() * nnum.pop()
print(result+sum(num1))