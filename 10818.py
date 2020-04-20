int(input())
b = input()

c = b.split()
c = list(map(int, c))

print(min(c), max(c))
