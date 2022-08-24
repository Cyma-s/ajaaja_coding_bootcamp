import sys
from bisect import bisect_left
input = sys.stdin.readline
n=int(input())
x =[int(i) for i in input().split()]
lis = []
for i in x:
    k = bisect_left(lis,i)
    if len(lis) <=k:
        lis.append(i)
    else:
        lis[k] = i
print(len(lis))