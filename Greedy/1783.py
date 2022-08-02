y, x = map(int, input().split())
if y==1:
    print(1)
elif y==2:
    print(min(4,(x-1)//2+1))
elif x<=6:
    print(min(4,x))
else:
    print(x-2)
