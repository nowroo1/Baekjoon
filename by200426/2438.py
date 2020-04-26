a = int(input())

for i in range(1, a+1):
    for j in range(i):
        print("*", end="")
    print("")

# a = int(input())
#
# for i in range(a):
#     print("*" * (i+1))