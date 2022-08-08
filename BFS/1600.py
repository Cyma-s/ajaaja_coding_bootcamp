from collections import deque
def bfs():
    q=deque()
    q.append((0,0,k))
    visit = [[[0 for _ in range(31)] for _ in range(m)] for _ in range(n)]
    while q:
        x,y,cnt = q.popleft()
        if x == (n-1) and y==(m-1):
            return visit[x][y][cnt]
        if cnt>0:
            for i in range(8):
                x2,y2 = x+dx_h[i], y+dy_h[i]
                if 0<=x2<n and 0<=y2<m and ground[x2][y2]==0 and visit[x2][y2][cnt-1]==0:
                    q.append((x2,y2,cnt-1))
                    visit[x2][y2][cnt-1] = visit[x][y][cnt]+1

        for j in range(4):
            x2,y2 = x+dx[j], y+dy[j]
            if 0<=x2<n and 0<=y2<m and ground[x2][y2]==0 and visit[x2][y2][cnt]==0:
                q.append((x2,y2,cnt))
                visit[x2][y2][cnt] = visit[x][y][cnt]+1
    return -1


dx = [0,1,0,-1]
dy = [1,0,-1,0]
dx_h=[-2,-2,-1,-1,1,1,2,2]
dy_h=[-1,1,-2,2,-2,2,-1,1]
k =int(input())
m,n = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]
print(bfs())
