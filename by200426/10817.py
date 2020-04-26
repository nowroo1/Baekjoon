put = input()
a = int(put.split()[0])
b = int(put.split()[1])
c = int(put.split()[2])

if a <= b:
    if b <= c:  # a <= b <= c
        print(b)
    else:  # a <= b, c < b
        if a <= c:  # a <= c < b
            print(c)
        else:  # c < a <= b
            print(a)
else:  # a > b
    if a <= c:  # b < a <= c
        print(a)
    else:  # b, c < a
        if b < c:  # b < c < a
            print(c)
        else:  # c < b < a
            print(b)
