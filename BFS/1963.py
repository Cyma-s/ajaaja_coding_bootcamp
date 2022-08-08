import sys, math
from collections import deque

def findPrime():
    for i in range(2, 100):
        if prime[i] == True:
            for j in range(2*i, 10000, i):
                prime[j] = False

def bfs():
    q = deque()
    q.append([start, 0])
    visited = [0 for i in range(10000)]
    visited[start] = 1

    while q:
        now, cnt = q.popleft()
        strNow = str(now)
        if now == end:
            return cnt

        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i+1:])
                if visited[temp] == 0 and prime[temp] and temp >= 1000:
                    visited[temp] = 1
                    q.append([temp, cnt + 1])


t = int(sys.stdin.readline())
prime = [True for _ in range(10000)]
findPrime()

for _ in range(t):
    start, end = map(int, sys.stdin.readline().split())
    result = bfs()
    print(result if result != None else "Impossible" )
