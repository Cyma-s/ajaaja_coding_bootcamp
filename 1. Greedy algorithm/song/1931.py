n = int(input())
time = []
for _ in range(n):
    time.append(tuple(map(int,input().split())))
time.sort(key=lambda x:(x[1],x[0]))
result=0
end=0
for s,e in time:
    if s>=end:
        result+=1
        end=e
print(result)