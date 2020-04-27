ct = 0

for i in range(8):
    a = input()
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0:
                if a[j] == 'F':
                    ct += 1
    else:
        for j in range(8):
            if j % 2 == 1:
                if a[j] == 'F':
                    ct += 1

print(ct)