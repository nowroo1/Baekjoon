a = int(input())
ct = 0

for i in range(a):
    ct += 1
    ex = list('abcdefghijklmnopqrstuvwxyz')
    e = input()
    k = ''
    for j in e:
        if k != '':
            if j != k:
                if j in ex:
                    ex.remove(k)
                else:
                    ct -= 1
                    break
        k = j



print(ct)
