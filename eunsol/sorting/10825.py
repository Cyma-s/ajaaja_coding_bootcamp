import sys
input = sys.stdin.readline
n = int(input())
_list = []
for _ in range(n):
    _list.append(input().rstrip().split())
sorted_list = [(-int(x[1]), int(x[2]), -int(x[3]), x[0]) for x in _list]
sorted_list.sort()
for x in sorted_list:
    print(x[3])