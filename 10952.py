a = list()

while True:
    b = input()
    data = b.split()

    if data[0] == '0' and data[1] == '0':
        break;

    a.append(int(data[0]))
    a.append(int(data[1]))

a.reverse()
while True:
    if len(a) == 0:
        break;
    print(a.pop() + a.pop())