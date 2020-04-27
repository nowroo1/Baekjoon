import sys

a, b = list(map(int, input().split()))
li1 = list()
ans = list()

for i in range(a):
    li1.append(sys.stdin.readline().rstrip())

for i in range(b):
    put = sys.stdin.readline().rstrip()
    if put in li1:
        ans.append(put)

ans.sort()

print(len(ans))
for i in ans:
    print(i)
