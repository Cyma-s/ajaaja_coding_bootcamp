import sys
input=sys.stdin.readline
n, c = map(int, input().split())
x =[int(input()) for _ in range(n)]
x.sort()
s=1
e = x[-1]-x[0]
result = 0

def bsearch():
    global s,e,result
    while s <= e:
        mid = (s + e) // 2
        now = x[0]
        count = 1
        for i in range(1, len(x)):
            if x[i] >= now + mid:
                count += 1
                now = x[i]

        if count >= c:
            s = mid + 1
            result = mid
        else:
            e = mid - 1

bsearch()
print(result)