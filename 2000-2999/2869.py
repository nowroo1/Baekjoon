import math

a, b, c = map(int, input().split())

dif = a - b
if (c - a) < 0:
    print(1)
else:
    print(math.ceil((c - b) / (a - b)))
