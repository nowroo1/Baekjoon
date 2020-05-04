a = int(input())

memo = [0, 1, 2, 4]


def dp(n):
    if n < len(memo):
        return memo[n]
    else:
        for j in range(len(memo), n+1):
            memo.append(memo[j-1]+memo[j-2]+memo[j-3])

        return memo[n]


for i in range(a):
    print(dp(int(input())))
