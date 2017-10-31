from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
#用坐标和半径表示一个圆
#namedtuple('名称',[属性list])
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)
print(c.x, c.y, c.r)

#Counter
from collections import Counter
c = Counter()
for ch in "programming":
    c[ch] += 1
print(c)