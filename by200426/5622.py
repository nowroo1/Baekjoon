a = input()
sm = 0

for i in a:
    n = ord(i)
    if n < 68:
        sm += 3
    elif n < 71:
        sm += 4
    elif n < 74:
        sm += 5
    elif n < 77:
        sm += 6
    elif n < 80:
        sm += 7
    elif n < 84:
        sm += 8
    elif n < 87:
        sm += 9
    else:
        sm += 10

print(sm)