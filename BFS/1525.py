from collections import deque

def bfs():
    q = deque()
    q.append(s)
    visit[s]=0
    while q:
        c = q.popleft()
        if c == 123456789:
            return visit[c]
        c2 = str(c)
        position = c2.find("9")
        x= position//3
        y= position%3
        for i in range(4):
            x2 = x+dx[i]
            y2 = y+dy[i]
            if 0<=x2<3 and 0<=y2<3:
                position2 = x2*3+y2
                t= list(c2)
                t[position2], t[position] = t[position], t[position2]
                t2 = int(''.join(t))
                if not visit.get(t2):
                    visit[t2] = visit[c]+1
                    q.append(t2)

    return -1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit=dict()
s = ""
for _ in range(3):
    temp = input()
    temp = temp.replace(" ","")
    s+=temp
s = int(s.replace("0","9"))
print(bfs())
