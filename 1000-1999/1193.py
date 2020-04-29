a = int(input())

n = 1


def sequence(i):
    return int(1 + (i ** 2 - i) / 2)


while a >= sequence(n + 1):
    n += 1

index = a - sequence(n)

if n % 2 == 1:
    print('%d/%d' % (n - index, index + 1))
else:
    print('%d/%d' % (index + 1, n - index))

