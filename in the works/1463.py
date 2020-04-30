a = int(input())
n = 0

while True:
    if a == 1:
        break
    else:
        if a % 3 == 0:
            a = a / 3
        elif a % 2 == 0:
            a = a / 2
        else:
            a -= 1
    n += 1

print(n)
