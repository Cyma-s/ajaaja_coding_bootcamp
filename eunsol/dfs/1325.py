import collections

n, m = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
count = [0] * (n+1)


def bfs(number):
    queue = collections.deque()
    queue.append(number)
    visited = [False] * (n+1)
    computer_count = 0
    while queue:
        computer = queue.popleft()
        if not visited[computer]:  # 방문한 적 X
            visited[computer] = True
            computer_count += 1
            for i in graph[computer]:
                queue.append(i)
    count[number] = computer_count


for i in range(1, n+1):
    bfs(i)
max_value = max(count)
for i in range(1, n+1):
    if max_value == count[i]:
        print(i, end=" ")