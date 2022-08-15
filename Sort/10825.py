n = int(input())
student = []
for _ in range(n):
    a,b,c,d = list(map(str, input().split()))
    student.append([a,int(b),int(c),int(d)])
student.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))
for i in student:
    print(i[0])
