import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
memo = dict()
for _ in range(n):
    _input = input().strip().split()
    memo[_input[0]] = _input[1]
for _ in range(m):
    print(memo[input().strip()])
