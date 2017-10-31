names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael':95, 'Bob':75, 'Tracy':85}
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))

print(d.pop('Bob'))
#dict内部存放的顺序和key放入的顺序是没有关系的
#和list想比较，dict有以下几个特点
#1.查找和插入的速度极快，不会随着key的增加而变慢
#2.需要占用大量的内存，内存浪费多

#而list相反：
#1.查找和插入的时间随着元素的增加而增加
#2.占用空间小，浪费内存很少

#所以，dict是用空间来换取时间的一种方法
#dict的key必须是不可变对象 这个通过key计算位置的算法称为哈希算法(Hash)
#在python中，字符串，整数等都是不可变的，因此，可以放心的作为key,而list是可变的，就不能作为key

#set和dict类似，也是一组key的集合，但不储存value。由于key不能重复，所以，在set中，没有重复的key
s = set([1,2,3])
print(s)

#重复元素在set中自动被过滤
s = set([1,1,2,2,3,3])
print(s)

s.add(4)
print(s)
s.remove(4)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合
#因此 两个set可以做数学意义上的交集，并集等操作
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)  #交集
print(s1 | s2)  #并集

#再议不可变对象
#对于可变对象，list内部内容是会变化的
a = ['c', 'b', 'a']
a.sort()
print(a)

#对于不可变对象，比如str
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)
#replace创建了一个新字符串'Abc'
#如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：