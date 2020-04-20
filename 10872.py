def recursion(i):
    if i == 1:
        return 1
    elif i == 0:
        return 1
    return i * recursion(i-1)


a = int(input())
print(recursion(a))
