def person(name, age, **kw):
    print('name', name, 'age', age, 'other:', kw)

person("Michael", 30)
person('Bob', 35, city='Beijing')

extra = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, **extra)

def person2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name', name, 'age', age, 'other:', kw)
person('Jack', 24, city="beijing")

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
# *args **kw

def person3(name, age, *, city, job):
    print(name, age, city, job)
#只接收city和job作为关键字参数
#命名一个关键字参数需要一个特殊分隔符*, *后面的参数被视为命名关键字参数
person3('philip', 26, city='Beijing', job='driver')

