import sys
input = sys.stdin.readline
guitar = []
for _ in range(int(input())):
    a = input().rstrip()
    sum = 0
    for i in a:
        if  i.isdigit():
            sum+=int(i)
    guitar.append((a,sum))

guitar.sort(key = lambda x:(len(x[0]),x[1],x[0]))
for i in guitar:
    print(i[0])
