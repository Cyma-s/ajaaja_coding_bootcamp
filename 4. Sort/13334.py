import sys
import heapq
input= sys.stdin.readline
n = int(input())
location = [sorted(list(map(int,input().split()))) for _ in range(n)]
d = int(input())
location.sort(key=lambda x:x[1])
people =[]
result = -1
for s,e in location:
    if s>= e-d:
        heapq.heappush(people,s)
    while people and people[0]<e-d:
        heapq.heappop(people)
    result =max(result,len(people))
print(result)