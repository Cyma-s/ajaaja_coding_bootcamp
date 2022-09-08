import sys
input = sys.stdin.readline
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * (1<<n-1) for _ in range(n)]

def tsp(i,r):
    if check[i][r] != 0:
        return check[i][r]

    if r == (1<<(n-1))-1:
        if w[i][0]:
            return w[i][0]
        else:
            return float('inf')

    min_r = float('inf')

    for j in range(1, n):
        if not w[i][j]:
            continue
        if r & (1<<j-1):
            continue
        d = w[i][j] + tsp(j, r | (1<<(j-1)))
        if min_r > d:
            min_r = d
    check[i][r] = min_r

    return min_r


print(tsp(0, 0))
