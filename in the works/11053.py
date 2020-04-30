n = int(input())
li = list(map(int, input().split()))
li2 = list()

k = min(li)

print(k)

for i in range(n):
    if li[i] == k:
        li2.append(li[i])
    