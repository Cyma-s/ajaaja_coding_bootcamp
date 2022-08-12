import sys
input = sys.stdin.readline
bulbs = []
for _ in range(10):
    bulb = list(input())
    for i in range(10):
        if bulb[i] == 'O':
            bulb[i] = 1
            continue
        bulb[i] = 0
    bulbs.append(bulb)
dx = [-1,1,0,0,0]
dy = [0,0,0,1,-1]
result =101
for b in range(1<<10):
    first  =[]
    for i in range(10):
        first.append(bulbs[i][:])
    cnt = 0
    for i in range(10):
        if b & (1<<i):
            cnt+=1
            for k in range():
                e