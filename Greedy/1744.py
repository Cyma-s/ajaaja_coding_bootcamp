import sys
input = sys.stdin.readline
n = int(input())
positive = []
negative = []
num = 0
for _ in range(n):
    a = int(input())
    if a>1:
        positive.append(a)
    elif a==1:
        num+=1
    else:
        negative.append(a)

positive.sort(reverse=True)
negative.sort()

if len(positive)%2==0:
    for i in range(0, len(positive), 2):
        num += positive[i]*positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        num += positive[i]*positive[i+1]
    num+= positive[len(positive)-1]

if len(negative)%2==0:
    for i in range(0, len(negative),2):
        num+= negative[i]*negative[i+1]
else:
    for i in range(0, len(negative)-1 , 2):
        num+= negative[i]*negative[i+1]
    num+= negative[len(negative)-1]

print(num)
