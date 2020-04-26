a = int(input())
li = list()

for i in range(a):
    b = input().split()
    ct = int(b[0])
    rt = ''
    for j in range(len(b[1])):
        rt += b[1][j] * ct
    li.append(rt)

for i in li:
    print(i)
