import sys
input = sys.stdin.readline
n,m = map(int,input().split())
site ={}
for _ in range (n):
    a,ps = input().split()
    site[a] =ps
for _ in range(m):
    print(site[input().rstrip()])