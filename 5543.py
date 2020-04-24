a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

m = 0
n = 0

if a < b:
    if a <= c: #a < b,c
        m = a
    else: #c < a < b
        m = c
else:
    if b <= c: #b < a,c
        m = b
    else: # c < b < a
        m = c

if d <= e:
    n = d
else:
    n = e

print(m + n - 50)

