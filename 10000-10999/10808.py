a = input()
li = list()

for i in range(26):
    li.append(0)

for i in a:
    n = ord(i)
    li[n-97] += 1

for i in li:
    print(i, end=" ")
