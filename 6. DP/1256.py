import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
word = [[1]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        word[i][j] = word[i-1][j] + word[i][j-1]
if word[n][m] <k:
    print(-1)
else:
    result =""
    while True:
        if n == 0 or m == 0:
            result += "z" * m
            result += "a" * n
            break
        if k<=word[n-1][m]:
            result += "a"
            n-=1
        else:
            result +="z"
            k -= word[n - 1][m]
            m-=1
            
    print(result)