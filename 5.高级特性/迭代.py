d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key, end=" ")
for key in d:
    print(d[key], end=" ")

for ch in 'ABC':
    print(ch, end = " ")

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

for key,value in enumerate(['A', 'B', 'C']):
    print(key, value)

#在for循环中，同时引用了两个变量，在python中是很常见的
for x,y in [(1, 1),(2,4),(3,9)]:
    print(x,y)

