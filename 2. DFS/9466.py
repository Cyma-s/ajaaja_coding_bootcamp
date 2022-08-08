import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(x):
    global result, cycle
    visited[x] = 1
    cycle.append(x)
    s = slist[x]
    if visited[s]:
        if s in cycle:
            result+= cycle[cycle.index(s):]
    else:
        dfs(s)
for _ in range(int(input())):
    n = int(input())
    slist = [0] + list(map(int,input().split()))
    visited = [1] +[0]*n
    result = []
    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-len(result))