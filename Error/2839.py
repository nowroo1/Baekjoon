for i in range(4900, 5001):
    a = str(i)

    lastIndex = a[-1]
    a = int(a)

    if a == 4 or a == 7:
        print(-1)
    elif lastIndex == '1' or lastIndex == '6':
        print(int(2 + (a - 6) / 5))
    elif lastIndex == '2' or lastIndex == '7':
        if a % 3 == 0:
            print(int(a / 3))
        elif a % 3 == 2:
            print(1 + int((a - 5) / 3))
        elif a % 3 == 1:
            print(2 + int((a - 10) / 3))
    elif lastIndex == '3' or lastIndex == '8':
        print(int(1 + (a - 3) / 5))
    elif lastIndex == '4' or lastIndex == '9':
        print(int(3 + (a - 9) / 5))
    elif lastIndex == '5' or lastIndex == '0':
        print(int(a / 5))