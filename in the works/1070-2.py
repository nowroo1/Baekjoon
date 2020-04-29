a, b = list(map(int, input().split()))

li = list()

t_x = 0
t_y = 0
ans = [0]

for i in range(a):
    put = input()
    li.append(put)
    if put.find('*') > 0:
        t_x = i
        t_y = put.index('*')
        li[t_x][t_y] = 1000001

obstacle = list(map(int, input().split()))


def path_end(x, y):
    if x-1 < 0 or x+1 >= a or y-1 < 0 or y + 1 >= b:
        return True
    else:
        paths = path_count(x, y)
        if paths == 0:
            return False
        elif len(paths) == 1:
            path_single(x, y, paths[0])


def path_count(x, y):
    count = 0
    direction = list()
    if li[x-1][y] != '-':
        count += 1
        direction.append('n')
    if li[x+1][y] != '-':
        count += 1
        direction.append('s')
    if li[x][y-1] != '-':
        count += 1
        direction.append('w')
    if li[x][y+1] != '-':
        count += 1
        direction.append('e')

    if count >= 2:
        return direction
    elif count == 1:
        return direction
    else:
        return 0


def path_single(x, y, d):
    if d == 'n':
        print(0)
    elif d == 's':
        print(0)
    elif d == 'e':
        print(0)
    else:
        obs = obstacle[ord(li[x][y-1]) - 65]
        if obs < li[x][y]:
            li[x][y-1] = obs


path_end(t_x, t_y)
print(sum(ans))
