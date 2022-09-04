import sys
input = sys.stdin.readline
n,m = map(int, input().split())
rank = [0]*(n+1)
parent = [i for i in range(n+1)]
line = [list(map(int,input().split())) for _ in range(m)]
line = sorted(line,key = lambda k : k[2])
ans = 0
end = 0

def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a,b = find(a),find(b)
    if a==b:
        return
    if rank[a] > rank[b]:
        parent[b]=a
    elif rank[a] < rank[b]:
        parent[a]=b
    else:
        parent[a]=b
        rank[b]+=1

for i in line:
    if find(i[0])!=find(i[1]):
        union(i[0],i[1])
        ans+=i[2]
        end = i[2]
print(ans - end)
