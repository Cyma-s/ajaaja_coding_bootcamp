import sys
input= sys.stdin.readline
n = int(input())
num = [input() for _ in range(n)]
def order(input):
    sum = 0
    for x in input:
        if x.isdigit():
            sum+=int(x)
    return sum
num.sort(key = lambda x:(len(x),order(x),x))
for x in num:
    print(x,end='')