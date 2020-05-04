import sys

n = int(sys.stdin.readline())
li = list()


def top():
    if len(li) == 0:
        print(-1)
    else:
        print(li[len(li) - 1])


def push(a):
    li.append(int(a[5:]))


def size():
    print(len(li))


def empty():
    if len(li) == 0:
        print(1)
    else:
        print(0)


def pop():
    if len(li) == 0:
        print(-1)
    else:
        print(li.pop())


for i in range(n):
    put = sys.stdin.readline().rstrip()

    if put == 'top':
        top()
    elif put == 'size':
        size()
    elif put == 'empty':
        empty()
    elif put == 'pop':
        pop()
    else:
        push(put)
