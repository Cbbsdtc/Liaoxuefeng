#None是不可变对象
#在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象
def add_end2(L=None):
    if L is None:
        L = []
    L.append("END")
    return L
print(add_end2())
print(add_end2())