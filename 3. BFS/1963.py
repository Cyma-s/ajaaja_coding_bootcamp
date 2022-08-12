import sys
from collections import deque
input=sys.stdin.readline
def findPrime(): #에라토스테네스의 체
    for i in range(2, 101):
        if prime[i] == True:
            j=2*i
            while j<10001:
                prime[j] = False
                j+=i
def bfs(s,e):
    q = deque()
    q.append([s, 0])
    visited = [0 for _ in range(10000)]
    visited[s] = 1
    while q:
        num, cnt = q.popleft()
        if num == e:
            return cnt
        for i in [1,10,100,1000]:
            temp = num-num%(i*10)//i*i
            for _ in range(10):
                if visited[temp] == 0 and prime[temp] and temp >= 1000:
                    visited[temp] = 1
                    q.append([temp, cnt + 1])
                temp += i
T = int(input())
prime = [True for _ in range(10001)]
visited = []
findPrime()
for _ in range(T):
    a,b = map(int, input().split())
    result = bfs(a,b)
    if result == None:
        print("Impossible")
    else:
        print(result)
