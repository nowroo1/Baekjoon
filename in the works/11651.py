import sys

n = int(sys.stdin.readline())
dic = {}

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    dic[a] = b

print(dic)

newDic = sorted(dic.items(), key=lambda t: t[1])

print(newDic)
