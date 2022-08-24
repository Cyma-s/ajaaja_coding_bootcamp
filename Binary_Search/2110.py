n,c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

end = arr[-1]-arr[0]
start=1
ans = 0
while start<=end:
    mid= (start+end)//2
    cnt = 1
    rou = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>= rou+mid:
            cnt+=1
            rou = arr[i]
    if cnt>=c:
        start = mid+1
        ans = mid
    else:
        end = mid-1

print(ans)
