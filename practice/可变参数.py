def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1,2,3,]))
print(calc([1,3,5,7]))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc2(1,2))
print(calc2(1,2,3,4))

num = [1,2,3]
print(num)
print(*num)