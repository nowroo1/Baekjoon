def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    return fibonacci(i-1) + fibonacci(i-2)

a = int(input())
print(fibonacci(a))