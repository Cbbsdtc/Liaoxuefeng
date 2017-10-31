def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 2))

def enroll(name, gender):
    print("name:", name)
    print("gender:", gender)
enroll('Sarah','F')

#默认参数降低了函数调用的难度，
#而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
def enroll(name, gender, age=6, city="Beijing"):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah', 'F')

def add_end(L=[]):
    L.append("END")
    return L

print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())

