import sys
input = sys.stdin.readline()
r,c = map(int,input.split())
place = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

if r%2==1:
    print(('R'*(c-1)+'D'+'L'*(c-1)+'D')*(r//2)+'R'*(c-1))
elif c%2==1:
    print(('D'*(r-1)+'R'+'U'*(r-1)+'R')*(c//2)+'D'*(r-1))
elif r%2==0 and c%2==0:
    low = 1000
    lowest = [-1, -1]
    for i in range(r):
        if i%2==0:
            for j in range(1,c,2):
                if low > place[i][j]:
                    low = place[i][j]
                    lowest = [i, j]

        else:
            for j in range(0,c,2):
                if low > place[i][j]:
                    low = place[i][j]
                    lowest = [i, j]

    move = ('D'*(r-1)+'R'+'U'*(r-1)+'R')*(lowest[1] // 2)
    x = 2*(lowest[1]//2)
    y = 0
    x2 = x+1
    while x!=x2 or y!=r-1:
        if x < x2 and [y,x2]!=lowest:
            x+=1
            move +='R'
        elif x==x2 and [y,x2-1]!=lowest:
            x-=1
            move +='L'
        if y!=r-1:
            y+=1
            move+='D'
    move+=('R'+'U'*(r-1)+'R'+'D'*(r-1))*((c-lowest[1]-1)//2)

    print(move)
