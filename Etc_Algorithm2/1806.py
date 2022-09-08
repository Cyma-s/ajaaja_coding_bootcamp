import sys
input = sys.stdin.readline

n,s = map(int, input().split())
arr = list(map(int,input().split()))
l,r = 0,0
tmp = 0
minl = sys.maxsize

while True:
    if tmp >= s:
        minl = min(minl, r-l)
        tmp -= arr[l]
        l +=1
    elif r==n:
        break
    else:
        tmp += arr[r]
        r+=1

if minl == sys.maxsize:
    print(0)
else:
    print(minl)
