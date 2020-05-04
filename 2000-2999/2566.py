max_a = 0
max_b = 0
max_n = 0

for i in range(9):
    a = list(map(int, input().split()))
    if max(a) > max_n:
        max_n = max(a)
        max_a = i+1
        max_b = a.index(max(a))+1

print(max_n)
print(max_a, max_b)