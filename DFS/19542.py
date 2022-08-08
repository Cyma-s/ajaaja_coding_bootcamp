import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
n,s,d = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
result =0

def dfs(x,y):
    global result
    cnt=0
    for i in graph[x]:
        if i!=y:
            cnt = max(cnt, dfs(i,x))
    if cnt >= d:
        result+=1
    return cnt+1


for _ in range(n-1):
    a,b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
dfs(s,0)
if result!=0:
    print(2*(result-1))
else:
    print(0)
