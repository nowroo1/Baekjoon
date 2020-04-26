def hansu(put):
    count = 99
    for i in range(100, put + 1):
        i = str(i)
        same = True
        for j in range(len(i) - 2):
            first = int(i[j + 1]) - int(i[j])
            second = int(i[j + 2]) - int(i[j + 1])
            if first != second:
                same = False

        if same:
            count += 1

    return count


a = int(input())
if a >= 100:
    a = hansu(a)
print(a)
