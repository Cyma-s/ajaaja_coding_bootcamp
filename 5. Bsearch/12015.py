import sys
input=sys.stdin.readline
n =int(input())
x =[int(i) for i in input().split()]
a = [0]
for i in range(n):
    s =0
    e = len(a)-1
    while s<=e:
        mid=(s+e)//2
        if a[mid]<x[i]:
            s = mid+1
        else:
            e = mid-1
    if s>=len(a):
      	a.append(x[i])
    else:
        a[s] = x[i]
print(len(a)-1)