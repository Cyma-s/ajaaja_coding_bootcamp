import sys
input = sys.stdin.readline
n= int(input())
arr = sorted(list(map(int,input().split())))
start = 0
end = n-1
a = abs(arr[start]+arr[end])
b = start
c = end

while start<end:
    tmp = arr[start]+arr[end]
    if abs(tmp)<a:
        b = start
        c = end
        a = abs(tmp)
        if a==0:
            break
    if tmp>0:
        end -=1
    else:
        start+=1

print(arr[b],arr[c])
