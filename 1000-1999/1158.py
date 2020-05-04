a, b = map(int, input().split())
li = list()
ans = list()
index = 0

for i in range(1, a+1):
    li.append(i)

while len(li) != 0:
    index = index + b - 1
    while index >= len(li):
        index -= len(li)

    ans.append(li.pop(index))

print('<', end="")
for i in range(len(ans)-1):
    print(ans[i], end=", ")
print(ans[len(ans)-1], end=">")
