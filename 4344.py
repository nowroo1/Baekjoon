a = int(input())
li = list()

for i in range(a):
    put = input().split()
    ct = int(put[0])
    del put[0]

    s = 0
    for j in put:
        s += int(j)

    mid = s / ct

    up = 0
    for j in put:
        if int(j) > mid:
            up += 1

    li.append(round(up/ct * 100, 3))

for i in li:
    print('%.3f%%' % i)