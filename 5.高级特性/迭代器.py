#for循环的数据类型有以下几种
#一类是集合数据类型，如list,tuple,dict,set,str
#一类是generator,包括生成器和带yield的generator function
#这些可以直接作用于for循环的对象统称为可迭代对象: Iterable
#可以使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
a = isinstance([], Iterable)
b = isinstance({}, Iterable)
c = isinstance('abc', Iterable)
d = isinstance((x for x in range(10)), Iterable)
e = isinstance(100, Iterable)
print(a, b, c, d, e)

#生成器都是Iterator对象，但list,dict,str虽然是Iterable，却不是Iterator
from collections import Iterator
f = isinstance((x for x in range(10)), Iterator)
g = isinstance([], Iterator)
h = isinstance({}, Iterator)
i = isinstance('abc', Iterator)
print(f, g, h, i)

#把list dict str等Iterable变成Iterator可以使用Iter()函数
j = isinstance(iter([]), Iterator)
k = isinstance(iter('abc'), Iterator)
print(j, k)

#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。