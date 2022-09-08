import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = dict()
for _ in range(n):
    a,b = map(str, input().split())
    s[a]=b
for _ in range(m):
    add = str(input().rstrip())
    print(s[add])
