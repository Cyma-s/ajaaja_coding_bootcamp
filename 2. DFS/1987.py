import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
r,c = map(int,input().split())
graph = [list(map(lambda a : ord(a)-65,input())) for _ in range(r)]
visited = [0] *26
x1 = [-1,1,0,0]
y1 = [0,0,-1,1]
result = 0
def dfs(x,y,cnt):
    global result
    result = max(cnt,result)
    for i in range(4):
        x2 = x + x1[i]
        y2 = y + y1[i]
        if 0<=x2<r and 0<=y2<c and visited[graph[x2][y2]] == 0:
            visited[graph[x2][y2]] = 1
            dfs(x2,y2,cnt+1)
            visited[graph[x2][y2]] = 0
visited[graph[0][0]] = 1
dfs(0,0,1)
print(result)