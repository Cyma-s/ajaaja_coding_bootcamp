import sys
input = sys.stdin.readline
def distance(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def dfs(cur):
    for j in range(n):
        if distance(location[cur], location[j])>(location[cur][2]+location[j][2])**2 or cur==j or visited[j]:
            continue
        visited[j]=True
        dfs(j)
t=int(input())
for _ in range(t):
    n=int(input())
    answer=0
    location=[]
    visited=[False for _ in range(n)]
    for _ in range(n):
        location.append(list(map(int, input().split())))
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
    print(answer)
