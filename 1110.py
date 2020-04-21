ans = int(input())
a = ans
total = 0


while True:
    total += 1
    if a < 10:
        a = '0' + str(a)

    aa = str(a)
    sm = int(aa[0]) + int(aa[1])

    if sm >= 10:
        sm = int(str(sm)[1])

    new = int(aa[1] + str(sm))
    if ans == new:
        print(total)
        break
    else:
        a = new
