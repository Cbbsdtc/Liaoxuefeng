class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
#给实例绑定属性是通过实例变量
s.score = 90
print(s.score)

#name是类属性，归Student类所有
class Student(object):
    name = "Student"

s = Student() #创建实例
print(s.name) #打印name属性，因为实例没有name属性，会继续找class的name属性
print(Student.name)
s.name = "Michael"
print(s.name)
print(Student.name)
del s.name
print(s.name)
