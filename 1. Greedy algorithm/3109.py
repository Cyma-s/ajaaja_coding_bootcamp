import sys
input=sys.stdin.readline
r,c = map(int,input().split())
near = [list(input()) for _ in range (r)]
visited = [[0]*c for _ in range(r)]
dx = [-1,0,1]
dy = [1,1,1]
cnt =0
def go(x,y):
    global cnt
    near[x][y] = 'o'
    if y ==c-1:
        cnt+=1
        return True
    for i in range(3):
        nx =x+dx[i]
        ny =y+dy[i]
        if 0<=nx<r and 0<=ny<c:
            if near[nx][ny] !='x' and near[nx][ny] !='o':
                if go(nx,ny):
                    return True
for i in range(r):
    go(i,0)
print(cnt)
