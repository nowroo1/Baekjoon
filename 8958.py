a = int(input())
pt = list()

for i in range(a):
    n = 0
    s = 0
    put = input()
    for j in range(len(put)):
        if put[j] == 'O':
            n += 1
            s += n
        else:
            n = 0
    pt.append(s)

for i in pt:
    print(i)
