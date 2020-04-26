import math

a = int(input())
p1 = ''
p2 = ''

for j in range(math.ceil(a / 2)):
    p1 += '* '

for j in range(int(a / 2)):
    p2 += ' *'

for i in range(a):
    print(p1)
    print(p2)
