import sys
input = sys.stdin.readline
n = int(input())
c=[]
for i in range(n):
    x,y,z = map(int, input().split())
    c.append((x,y,z,i))

edge = []
for i in range(3):
    c.sort(key=lambda x: x[i])
    for j in range(1,n):
        edge.append((abs(c[j-1][i] - c[j][i]), c[j-1][3],c[j][3]))
parent = [i for i in range(n)]
cnt =0
edge.sort()

def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(len(edge)):
    if find(edge[i][1]) != find(edge[i][2]):
        union(edge[i][1], edge[i][2])
        cnt += edge[i][0]

print(cnt)

