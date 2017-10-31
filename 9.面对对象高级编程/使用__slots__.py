#限制实例属性,Student实例只能含有name和age的属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = "Michael"
s.age = 25
s.score = 99

#__slot__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GranduateStudent(Student):
    pass

g = GranduateStudent()
g.score = 9999

#除非在子类中也定义__slots__，这样
#子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

