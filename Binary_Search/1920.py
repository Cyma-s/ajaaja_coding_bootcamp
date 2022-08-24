import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
m = int(input())
arr = list(map(int,input().split()))
a.sort()

for i in arr:
    start=0
    end=n-1
    b = False

    while start <= end:
        mid=(start+end)//2
        if i == a[mid]:
            b= True
            print(1)
            break
        elif i>a[mid]:
            start = mid+1
        else:
            end = mid -1
    if not b:
        print(0)
