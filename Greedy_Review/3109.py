import sys
input = sys.stdin.readline
r,c = map(int, input().split())
table = [list(input().rstrip()) for _ in range(r)]
dx=[-1,0,1]
dy=[1,1,1]
visit = [[False]*c for _ in range(r)]
cnt= 0
def solve(a,b):
    if b==c-1:
        return True
    for i in range(3):
        x = a+dx[i]
        y = b+dy[i]
        if(0<=x<r) and (0<=y<c) and not visit[x][y] and table[x][y] ==".":
            visit[x][y] = True
            if solve(x,y):
                return True
    return False

for i in range(r):
    if table[i][0]==".":
        if solve(i,0):
            cnt+=1
print(cnt)
