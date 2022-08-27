import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
w = int(input())
pos = [(1,1),(n,n)]
check = [[-1] * (w+2) for _ in range(w+2)]
for _ in range(w):
    pos.append(tuple(map(int,input().split())))

def search(x,y):
    if x> w or y > w:
        return 0
    if check[x][y]!=-1:
        return check[x][y]
    next_p = max(x,y)+1
    nr = search(next_p,y) + abs(pos[next_p][0] - pos[x][0]) + abs(pos[next_p][1] - pos[x][1])
    nc = search(x,next_p) + abs(pos[next_p][0] - pos[y][0]) + abs(pos[next_p][1] - pos[y][1])
    check[x][y] = min(nr,nc)
    return check[x][y]

def route(x,y):
    if x>w or y>w:
        return
    next_p = max(x,y)+1
    nr = abs(pos[next_p][0] - pos[x][0]) + abs(pos[next_p][1] - pos[x][1])
    nc = abs(pos[next_p][0] - pos[y][0]) + abs(pos[next_p][1] - pos[y][1])

    if check[next_p][y] + nr < check[x][next_p] + nc:
        print(1)
        route(next_p, y)
    else:
        print(2)
        route(x, next_p)
    return


print(search(0,1))
route(0,1)
