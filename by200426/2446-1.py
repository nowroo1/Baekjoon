a = int(input())
n = 2 * a - 1

for i in range(a, 0, -1):
    print('{:^{w}}'.format('*' * (2 * i - 1), w=n))

for i in range(1, a):
    print('{:^{w}}'.format('*' * (2 * i + 1), w=n))