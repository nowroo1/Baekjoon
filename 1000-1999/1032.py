n = int(input())
li = list()
ans = ''

for i in range(n):
    li.append(input())

for i in range(len(li[0])):
    same = True
    for j in range(n - 1):
        if li[j][i] != li[j + 1][i]:
            same = False
    if same:
        ans += li[0][i]
    else:
        ans += '?'

print(ans)
