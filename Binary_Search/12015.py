import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
s = [0]
for i in range(n):
    low = 0
    high = len(s)-1
    while low<=high:
        mid = (low+high)//2
        if s[mid] < a[i]:
            low = mid+1
        else:
            high = mid -1
    if low>=len(s):
        s.append(a[i])
    else:
        s[low] = a[i]
print(len(s)-1)
