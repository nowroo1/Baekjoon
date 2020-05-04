a, b = map(int, input().split())
li = list()
n = 0

for i in range(a):
    li.append(int(input()))

li.reverse()

for i in li:
    if b//i > 0:
        n += b//i
        b -= i * (b//i)
    else:
        pass

print(n)
