import sys
input=sys.stdin.readline
n = int(input())
x =[int(i) for i in input().split()]
x.sort()
si = 0
ei = n-1
result = x[si]+x[ei]
s =si
e =ei
while si<ei:
    tmp = x[si]+x[ei]
    if abs(tmp)< abs(result):
        result = tmp
        s=si
        e=ei
        if result == 0:
            break
    if tmp<0:
        si+=1
    else:
        ei-=1
print(x[s],x[e])