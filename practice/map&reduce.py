#map sample
#map函数含有两个参数 第一个参数为函数，第二个参数为赋值列表
def f(x):
    return x * x
r = map(f, [1,2,3,4,5,6,7,8,9,10])
print(list(r))

L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(n)
print(L)

a = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(a)

from functools import reduce
def add(x,y):
    return x+y
s = reduce(add, [1,3,5,7,9])
print(s)

def fn(x,y):
    return x*10+y
t = reduce(fn, [1,3,5,7,9])
print(t)

def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
k = reduce(fn, map(char2num, '13579'))

