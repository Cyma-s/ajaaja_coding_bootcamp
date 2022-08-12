import sys
input = sys.stdin.readline
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
crane.sort(reverse=True)
box.sort(reverse=True)

if box[0] > crane[0]:
    print(-1)
else:
    cnt = 0
    while box:
        if not box:
            break
        for i in crane:
            for j in box:
                if i>=j:
                    box.remove(j)
                    break

        cnt+=1

    print(cnt)
