sm = 1

for i in range(3):
    sm *= int(input())

for i in range(10):
    print(str(sm).count(str(i)))
