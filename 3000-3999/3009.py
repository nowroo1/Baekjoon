x_a, y_a = map(int, input().split())
x_b, y_b = map(int, input().split())
x_c, y_c = map(int, input().split())

x_d = 0
y_d = 0

if x_a == x_b:
    x_d = x_c
elif x_a == x_c:
    x_d = x_b
else:
    x_d = x_a

if y_a == y_b:
    y_d = y_c
elif y_a == y_c:
    y_d = y_b
else:
    y_d = y_a

print(x_d, y_d)
