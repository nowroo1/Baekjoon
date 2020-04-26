def solve(a) -> int:
    sum = 0
    for i in a:
        sum += i
    return sum


ex = [1, 4, 3, 2, 14, 2]

print(solve(ex))
