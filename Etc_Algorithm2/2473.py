import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
minl = sys.maxsize
for i in range(n-2):
    s = i+1
    e = n-1
    while s<e:
        tmp = arr[i]+arr[s]+arr[e]
        if abs(tmp)<minl:
            minl = abs(tmp)
            ans = [arr[i],arr[s],arr[e]]
        if tmp<0:
            s+=1
        elif tmp>0:
            e-=1
        else:
            break

print(ans[0],ans[1],ans[2])
