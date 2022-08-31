from collections import deque
max = 100001
n,k = map(int,input().split())
q = deque()
q.append(n)
check = [-1 for _ in range(max)]
check[n] = 0

while q:
    a = q.popleft()
    if a == k:
        print(check[k])
        break
    if 0<=a*2 < max and check[a*2] == -1:
        q.appendleft(a*2)
        check[a*2] = check[a]
    if 0<=a + 1 < max and check[a+1] == -1:
        q.append(a+1)
        check[a+1] = check[a]+1
    if 0<=a - 1 < max and check[a-1] == -1:
        q.append(a-1)
        check[a-1] = check[a]+1
