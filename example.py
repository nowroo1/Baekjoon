count = 0


def fibonacci(a):
    global count
    if a <= 2:
        count += 1
        return 1
    else:
        count += 1
        return fibonacci(a - 1) + fibonacci(a - 2)


n = int(input())
fibonacci(n)
print(count)
