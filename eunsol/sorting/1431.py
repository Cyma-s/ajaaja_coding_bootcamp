def cal_sum(string):
    return sum([int(j) for j in string if j.isdigit()])


n = int(input())
serial = [input() for _ in range(n)]
sorted_serial = [(len(x), cal_sum(x), x) for x in serial]
sorted_serial.sort()
for length, x_sum, x in sorted_serial:
    print(x)
