a = list()
sum = 0

for i in range(5):
    b = int(input())

    if (b < 40):
        b = 40

    sum += b

print(int(sum / 5))