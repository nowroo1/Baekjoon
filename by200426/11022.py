import sys

number = int(input())
data = list()

for i in range(number):
    a = sys.stdin.readline()
    inp = a.split()
    data.append(inp[0])
    data.append(inp[1])

data.reverse()
data = list(map(int, data))

for i in range(int(len(data) / 2)):
    a = data.pop()
    b = data.pop()
    print("Case", "#%d:" % (i + 1), a, "+", b, "=", (a + b))
