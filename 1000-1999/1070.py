a, b = list(map(int, input().split()))

li = list()

t_x = 0
t_y = 0
ans = list()

for i in range(a):
    put = input()
    li.append(put)
    if put.find('*') > 0:
        t_x = i
        t_y = put.index('*')

obstacle = list(map(int, input().split()))


def northBound(x, y):
    tem_ans = 1000001
    while x >= 0:
        if li[x][y] == '-':
            tem_ans = 1000001
            break;
        else:
            obs = obstacle[ord(li[x][y])-65]
            if obs < tem_ans:
                tem_ans = obs
        x -= 1

    if tem_ans < 1000001:
        ans.append(tem_ans)


def southBound(x, y):
    tem_ans = 1000001
    while x < b:
        if li[x][y] == '-':
            tem_ans = 1000001
            break;
        else:
            obs = obstacle[ord(li[x][y]) - 65]
            if obs < tem_ans:
                tem_ans = obs
        x += 1

    if tem_ans < 1000001:
        ans.append(tem_ans)


def westBound(x, y):
    tem_ans = 1000001
    while y >= 0:
        if li[x][y] == '-':
            tem_ans = 1000001
            break;
        else:
            obs = obstacle[ord(li[x][y]) - 65]
            if obs < tem_ans:
                tem_ans = obs
        y -= 1

    if tem_ans < 1000001:
        ans.append(tem_ans)


def eastBound(x, y):
    tem_ans = 1000001
    while y < a:
        if li[x][y] == '-':
            tem_ans = 1000001
            break;
        else:
            obs = obstacle[ord(li[x][y]) - 65]
            if obs < tem_ans:
                tem_ans = obs
        y += 1

    if tem_ans < 1000001:
        ans.append(tem_ans)


northBound(t_x-1, t_y)
southBound(t_x+1, t_y)
westBound(t_x, t_y-1)
eastBound(t_x, t_y+1)

print(sum(ans))
