L = [x * x for x in range(10)]
print(L)
#g is a generator
g = (x * x for x in range(10))
print(g)
for x in g:
    print(x, end=' ')

#Fibonacci数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=' ')
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(10))

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib2(6):
    print(n, end=" ")

g = fib2(6)
while True:
    try:
        x = next(g)
        print('g', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

