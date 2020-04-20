a = list()

for i in range(10000):
    a.append(i + 1)

for i in range(1, 10000):
    sm = 0
    for j in range(len(str(i))):
        aNumber = int(str(i)[j])
        sm += aNumber

    sm += i
    if sm <= 10000 and sm in a:
        a.remove(sm)

print(*a, sep="\n")
