n=int(input())
a = list(map(int, input().split(' ')))
a.sort()
m=int(input())
b= list(map(int, input().split(' ')))

for i in b:
    left, right =0, len(a)-1
    found=False
    while True:
        mid=(left+right)//2
        if i==a[mid]:
            found=True
            print(1)
            break
        elif i>a[mid]:
            left=mid+1
        elif i<a[mid]:
            right=mid-1
        if left>right:
            break
    if not found:
        print(0)