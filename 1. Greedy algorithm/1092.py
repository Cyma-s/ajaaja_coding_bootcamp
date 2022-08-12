import sys
input = sys.stdin.readline
n=int(input())
cweight = list(map(int,input().split()))
m = int(input())
bweight = list(map(int,input().split()))
cweight.sort(reverse=True)
bweight.sort(reverse=True)
if bweight[0] > cweight[0]:
    print(-1)
else:
    time = 0
    while bweight:
        if not bweight:
            break
        for crane in cweight:
            for box in bweight:
                if crane >= box:
                    bweight.remove(box)
                    break
        time+=1
    print(time)