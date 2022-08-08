import sys
from collections import deque
sys.setrecursionlimit(10000)


def solve(number):
    for j in range(4):
        for k in range(10):
            changed_number = change_number(number, j, k)
            if changed_number != number and changed_number in primes:
                if visited[changed_number] > visited[number] + 1:
                    visited[changed_number] = visited[number] + 1
                    queue.append(changed_number)
    while queue:
        num = queue.popleft()
        solve(num)


def change_number(number, index, change):
    temp = str(number)
    temp = temp[:index] + str(change) + temp[index+1:]
    return int(temp)


t = int(input())
primes = [True] * 10001
for i in range(2, 10001):
    if not primes[i]:
        continue
    for j in range(i+i, 10001, i):
        primes[j] = False
primes = [i for i in range(1000, 10001) if primes[i]]
for _ in range(t):
    queue = deque()
    result = sys.maxsize
    visited = [sys.maxsize] * 10000
    a, b = map(int, input().split())
    visited[a] = 0
    solve(a)
    if visited[b] == sys.maxsize:
        print("Impossible")
    else:
        print(visited[b])