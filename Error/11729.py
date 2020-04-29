a = int(input())


def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, via, to)
        print(start, to)
        hanoi(n-1, via, to, start)


print(a)
hanoi(a, 1, 3, 2)
