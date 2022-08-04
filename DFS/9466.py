import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(p):
    global result
    visit[p] = 1
    team.append(p)
    num = point[p]
    if visit[num]==1:
        if num in team:
            result += team[team.index(num):]
        return
    else:
        dfs(num)


cnt = int(input())
for _ in range(cnt):
    n = int(input())
    point = [0]+list(map(int, input().split()))
    visit = [0]*(n+1)
    result = []

    for i in range(1, n+1):
        if not visit[i]:
            team = []
            dfs(i)

    print(n-len(result))
