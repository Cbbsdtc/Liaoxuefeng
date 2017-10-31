L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-2:])
print(L[-2:-1])

L2 = list(range(100))
print(L2)
print(L2[:10])
print(L2[-10:])
print(L2[10:20])
print(L2[:10:2])
print(L2[::5])
print(L[:])

#tuple也是一种list,唯一区别是tuple不可变
print((0,1,2,3,4,5)[:3])
#字符串也是一种list
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

