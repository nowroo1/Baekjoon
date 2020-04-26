data = input()

convert = data.split()

a = list(map(int, convert))

print((a[0]+a[1])%a[2])
print(((a[0]%a[2])+(a[1]%a[2]))%a[2])
print((a[0]*a[1])%a[2])
print(((a[0]%a[2])*(a[1]%a[2]))%a[2])