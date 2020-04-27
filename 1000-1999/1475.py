a = input()

s = [0, 0, 0, 0, 0, 0, 0, 0, 0]

h = True

for i in a:
    if i == '6' or i == '9':
        if h:
            h = False
            s[6] += 1
        else:
            h = True
    else:
        s[int(i)] += 1

print(max(s))