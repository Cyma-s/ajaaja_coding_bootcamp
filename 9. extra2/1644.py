import math
import sys
input = sys.stdin.readline
n = int(input())
prime_num =[]
prime = [0,0] +[1]*(n-1)
for i in range(2,n+1):
    if prime[i]:
        prime_num.append(i)
        for j in range(2*i,n+1,i):
            prime[j] =0
result,sum,s,e=0,0,0,0
while (True):
    if sum ==n:
        result+=1
    if sum >n:
        sum-=prime_num[s]
        s+=1
    elif e==len(prime_num):
        break
    else:
        sum += prime_num[e]
        e+=1
print(result)