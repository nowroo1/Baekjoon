n = int(input())
ans = list()

for i in range(n):
    a, b = map(int, input().split(','))
    ans.append(a+b)

for i in ans:
    print(i)