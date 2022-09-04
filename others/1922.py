import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
line = [list(map(int,input().split())) for _ in range(m)]
line = sorted(line,key = lambda k : k[2])
parent = [i for i in range(n+2)]
ans = 0

def find(x):
    if x== parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x,y = find(x),find(y)
    parent[x]=y

for i in line:
    start, end, wei =i
    if find(start) == find(end):
        continue
    else:
        ans+=wei
        union(start,end)
print(ans)
