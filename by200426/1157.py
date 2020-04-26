a = input()
li = list()

for i in range(26):
    li.append(0)

for i in a:
    n = ord(i)
    if 64 < n < 91:
        li[n-65] += 1
    else:
        li[n-97] += 1

li2 = li[:]
li2.sort()
if li2.pop() == li2.pop():
    print('?')
else:
    print(chr(li.index(max(li)) + 65))
