a = int(input())

n = 1


while True:
    if 3*n*n - 3*n + 2 <= a:
        n += 1
    else:
        break

print(n)
