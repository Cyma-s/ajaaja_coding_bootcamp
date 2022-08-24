import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
s = [a[0]]
for i in a[1:]:
    if s[-1]<i:
        s.append(i)
    else:
        start = 0
        end = len(s)-1
        while start<end:
            mid = (start+end)//2
            if s[mid]<i:
                start = mid+1
            else:
                end = mid
        s[end]=i
print(len(s))
