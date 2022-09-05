import math
import sys
input = sys.stdin.readline
t = int(input())
def union(x):
    if parent[x] ==x:
        return x
    parent[x] = union(parent[x])
    return parent[x]
def find(i,j):
    parent1 = union(i)
    parent2 = union(j)
    if parent1>parent2:
        parent[parent1] =parent2
    else:
        parent[parent2] = parent1

for _ in range(t):
    n = int(input())
    c = [list(map(int,input().split())) for _ in range(n)]
    parent = [i for i in range(n)]
    for i in range(n):
        x,y,r = c[i]
        for j in range(i+1,n):
            x1,y1,r1 = c[j]
            if math.sqrt((x-x1)**2 + (y-y1)**2) <=r+r1:
                find(i,j)
    count = set()
    for i in range(n):
        x= union(i)
        if x not in count:
            count.add(x)
    print(len(count))