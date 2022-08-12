import sys
input = sys.stdin.readline
n,k= map(int,input().split())
order = list(map(int,input().split()))
tap = []
cnt = 0
for i in range(k):
    if order[i] in tap:
        continue
    if len(tap) != n:
        tap.append(order[i])
        continue
    nouse = 0
    temp = 0
    for plug in tap:
        if plug not in order[i:]:
            temp = plug
            break
        elif order[i:].index(plug)>nouse:
            nouse = order[i:].index(plug)
            temp = plug
    tap[tap.index(temp)] = order[i]
    cnt+=1
print(cnt)