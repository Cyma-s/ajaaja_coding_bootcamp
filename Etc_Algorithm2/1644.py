import sys
input = sys.stdin.readline

n = int(input())
arr = []
prime = [False,False]+[True]*(n-1)
for i in range(2,int(n**0.5)+1):
    if prime[i]:
        prime[i*2::i] = [False]*((n-i)//i)

for i in range(n+1):
    if prime[i]:
        arr.append(i)

cnt , sum= 0,0
i,j=0,0
while (True):
    if sum==n:
        cnt+=1
    if sum>n:
        sum-=arr[i]
        i+=1
    elif j==len(arr):
        break
    else:
        sum+=arr[j]
        j+=1

print(cnt)
