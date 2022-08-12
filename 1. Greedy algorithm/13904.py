import sys
input = sys.stdin.readline
n =int(input())
homework = [list(map(int,input().split())) for _ in range(n)]
homework.sort(key = lambda x:x[1],reverse=True)
answer = 0
visited = [0]*1001
for d,w in homework:
    temp = d
    while temp > 0 and visited[temp]:
        temp -= 1
    if temp == 0:
        continue
    else:
        visited[temp] = True
        answer  += w
print(answer)