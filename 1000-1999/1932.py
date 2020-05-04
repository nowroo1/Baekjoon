n = int(input())
ans = [0 for i in range(n+2)]

for i in range(n):
    li = list(map(int, input().split()))
    pre = ans[:]
    for j in range(len(li)):
        if pre[j] > pre[j+1]:
            ans[j+1] = pre[j] + li[j]
        else:
            ans[j+1] = pre[j+1] + li[j]

print(max(ans))
