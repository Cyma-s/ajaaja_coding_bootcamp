import sys
input= sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
minval = sys.maxsize
if n==3:
    print(*arr)
    sys.exit()
for i in range(n-2):
    a = arr.pop()
    s,e=0,len(arr)-1
    while (s!=e):
        sum = a+arr[s]+arr[e]
        if minval>abs(sum):
            minval=abs(sum)
            answer =(a,arr[s],arr[e])
        if sum<minval:
            s+=1
        else:
            e-=1
        if minval==0:
            break
print(*sorted(answer))