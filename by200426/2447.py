def recursion(i):
    if i == 1:
        return
    print("*" * i)
    print("* *")
    print("*" * i)
    recursion(int(i/3))


a = int(input())
recursion(a)
