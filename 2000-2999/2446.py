a = int(input())
n = 2 * a - 1

for i in range(a):
    print(' ' * i + '*' * (n - 2 * i))

for i in range(a-2, -1, -1):
    print(' ' * i + '*' * (n - 2 * i))
