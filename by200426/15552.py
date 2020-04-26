import sys

number = int(input())
answer = list()

for i in range(number):
    a = sys.stdin.readline()
    data = a.split()
    answer.append(int(data[0])+int(data[1]))

for i in answer:
    print(i)