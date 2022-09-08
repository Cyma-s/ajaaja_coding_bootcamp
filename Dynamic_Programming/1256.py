import sys
input = sys.stdin.readline
n,m,k = map(int, input().split())
check = [[1] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        check[i][j] = check[i-1][j]+check[i][j-1]

if check[n][m] < k:
    print(-1)
else:
    result = ""
    while True:
        if n==0 or m==0:
            result += "z"*m
            result += "a"*n
            break

        flag = check[n-1][m]
        if k<= flag:
            result += "a"
            n -=1
        else:
            result +="z"
            m-=1
            k -= flag
    print(result)
