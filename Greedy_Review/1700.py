n,k = map(int,input().split())
item = list(map(int,input().split()))
tap = []
cnt = 0
for i,j in enumerate(item):
    if j in tap:
        continue
    if len(tap) < n:
        tap.append(j)
    else:
        a = 0
        index = -1
        cnt += 1
        tmp = item[i:]
        for x in tap:
            if x in tmp:
                b = tmp.index(x)
                if index < b:
                    index = b
                    a = x
            else:
                a = x
                break
        tap[tap.index(a)] = j

print(cnt)
