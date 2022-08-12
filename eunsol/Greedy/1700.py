n, k = map(int, input().split())
_list = list(map(int, input().split()))
plugs = []
result = 0
for i in range(len(_list)):
    if _list[i] in plugs:
        continue
    if len(plugs) < n:
        plugs.append(_list[i])
    else:  # 아예 없으면
        max_index = 0
        max_value = 0
        for plug in plugs:
            if plug not in _list[i:]:
                max_value = plug
                break
            if _list[i:].index(plug) > max_index:
                max_value = plug
                max_index = _list[i:].index(plug)
        plugs[plugs.index(max_value)] = _list[i]
        result += 1
print(result)
