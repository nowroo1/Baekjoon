a, b = list(map(int, input().split()))
n = 0
ans = ''

if a == 1 or a == 10:
    n = b % 7
elif a == 2 or a == 3 or a == 11:
    n = (b + 3) % 7
elif a == 4 or a == 7:
    n = (b + 6) % 7
elif a == 5:
    n = (b + 1) % 7
elif a == 6:
    n = (b + 4) % 7
elif a == 8:
    n = (b + 2) % 7
elif a == 9 or a == 12:
    n = (b + 5) % 7

if n == 0:
    ans = 'SUN'
elif n == 1:
    ans = 'MON'
elif n == 2:
    ans = 'TUE'
elif n == 3:
    ans = 'WED'
elif n == 4:
    ans = 'THU'
elif n == 5:
    ans = 'FRI'
elif n == 6:
    ans = 'SAT'

print(ans)