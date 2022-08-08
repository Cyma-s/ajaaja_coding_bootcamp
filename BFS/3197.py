from collections import deque
import sys

input= sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n,m = map(int, input().split())
visit = [[0]*m for _ in range(n)]
visit2 = [[0]*m for _ in range(n)]
lake = [list(input().rstrip()) for _ in range(n)]
water, tmp_water,swan, tmp_swan = deque(),deque(),deque(),deque()
ey,ex,ans=0,0,0
def water_board():
    while water:
        y,x = water.popleft()
        lake[y][x] = "."
        for i in range(4):
            y2 = y+dy[i]
            x2 = x+dx[i]
            if y2<0 or y2>=n or x2<0 or x2>=m or visit[y2][x2]:
                continue
            if lake[y2][x2]==".":
                water.append((y2,x2))
            else:
                tmp_water.append((y2,x2))
            visit[y2][x2]=True

def swan_board():
    while swan:
        y,x = swan.popleft()
        if y==ey and x==ex:
            return True
        for i in range(4):
            y2 = y+dy[i]
            x2 = x+dx[i]
            if y2 < 0 or y2 >= n or x2 < 0 or x2 >= m or visit2[y2][x2]:
                continue
            if lake[y2][x2] == ".":
                swan.append((y2, x2))
            else:
                tmp_swan.append((y2, x2))
            visit2[y2][x2] = True
    return False

for i in range(n):
    for j in range(m):
        if lake[i][j] =="L":
            if not swan:
                swan.append((i,j))
                visit2[i][j]=True
            else:
                ey,ex=i,j
            lake[i][j]="."
        if lake[i][j] ==".":
            water.append((i,j))
            visit[i][j]=True

while True:
    water_board()
    if swan_board():
        break
    water= tmp_water
    swan = tmp_swan
    tmp_water =deque()
    tmp_swan= deque()
    ans+=1

print(ans)
