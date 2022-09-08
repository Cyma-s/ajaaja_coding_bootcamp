import sys
input = sys.stdin.readline
n,s = map(int,input().split())
num = list(map(int,input().split()))
left , right =0,0
sum =0
minl= sys.maxsize
while True:
    if sum>=s:
        minl = min(minl,right-left)
        sum -= num[left]
        left+=1
    elif right == n:
        break
    else:
        sum += num[right]
        right+=1
if minl == sys.maxsize:
    print(0)
else:
    print(minl)