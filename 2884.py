data = input()

a = data.split()

num1 = int(a[0])
num2 = int(a[1])

if num2 < 45:
    if num1 == 0:
        print(23,num2+15)
    else:
        print(num1-1,num2+15)

else:
    print(num1,num2-45)