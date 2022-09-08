import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
target = sum(arr)
answer =0
temp =arr[0]
for i in range(1,n): #ㅂㅂㄲ
    temp+=arr[i]
    answer =max(answer,target-arr[0]+target-temp-arr[i])
arr.reverse()
temp =arr[0]
for i in range(1,n): #ㄲㅂㅂ
    temp+=arr[i]
    answer =max(answer,target-arr[0]+target-temp-arr[i])
for i in range(1,n):
    answer= max(answer,target-arr[0]-arr[-1]+arr[i])
print(answer)