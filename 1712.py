import sys

data = sys.stdin.readline()
data = data.split()
ls = list(map(int, data))
a = ls[0]
b = ls[1]
c = ls[2]

if (c - b) == 0:
    print(-1)
else:
    ans = a / (c - b)

    if ans < 0:
        print(-1)
    else:
        print(int(ans) + 1)
