print(type(123))

print(type(abs))

import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)
#isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
#object -> Animal -> Dog -> Husky
#isinstance(h, Husky)  True
#isinstance(h. Dog)    True
#能用type()判断的基本类型也可以用isinstance()判断

