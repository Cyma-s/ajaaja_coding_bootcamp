import sys
input = sys.stdin.readline
n,m = map(int,input().split())
answer = m-n +1
ssarr = [0]*answer
for i in range(2,int(m**0.5+1)):
    square= i**2
    for j in range((((n-1)//square)+1)*square,m+1,square):
        if not ssarr[j-n]:
            ssarr[j-n]=1
            answer-=1
print(answer)