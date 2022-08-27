import sys
n,k = map(int, input().split())
bag = [[0,0]]
result = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    bag.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1, k+1):
        w = bag[i][0]
        v= bag[i][1]

        if j<w:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j], result[i-1][j-w]+v)

print(result[n][k])
