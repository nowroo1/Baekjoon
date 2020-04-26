a = int(input())
b = list(map(int, input().split()))
sm = 0

for i in range(a):
    sm += int(b[i])

print(sm / max(b) / a * 100)