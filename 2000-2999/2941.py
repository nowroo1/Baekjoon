a = input()
ct = 0
sv = ''


def exist(c):
    if c == 'c' or c == 'd' or c == 'l' or c == 'n' or c == 's' or c == 'z':
        return True
    else:
        return False


for i in a:
    if sv == '':
        ct += 1
        if exist(i):
            sv = i
    elif sv == 'c':
        if i == '=' or i == '-':
            sv = ''
            continue
        else:
            if exist(i):
                sv = i
            ct += 1
    elif sv == 'd':
        if i == 'z':
            sv = 'dz'
            ct += 1
            continue
        if i == '-':
            sv = ''
            continue
        else:
            if exist(i):
                sv = i
            ct += 1
    elif sv == 'dz':
        if i == '=':
            ct -= 1
            sv = ''
            continue
        else:
            if exist(i):
                sv = i
            ct += 1
    elif sv == 'l':
        if i == 'j':
            sv = ''
            continue
        else:
            if exist(i):
                sv = i
            ct += 1
    elif sv == 'n':
        if i == 'j':
            sv = ''
            continue
        else:
            if exist(i):
                sv = i
            ct += 1
    elif sv == 's':
        if i == '=':
            sv = ''
            continue
        else:
            if exist(i):
                sv = i
            ct += 1
    elif sv == 'z':
        if i == '=':
            sv = ''
            continue
        else:
            if exist(i):
                sv = i
            ct += 1

print(ct)