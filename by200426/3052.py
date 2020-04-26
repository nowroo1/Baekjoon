li = list()

for i in range(10):
    a = int(input()) % 42
    if not a in li:
        li.append(a)

print(len(li))