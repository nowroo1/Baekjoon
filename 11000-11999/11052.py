n = int(input())
ex = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    k = ex[i]
    for j in range(1, int(i/2) + 1):
        m = ex[i-j] + ex[j]
        if m > k:
            k = m
    ex[i] = k

print(ex[n])
