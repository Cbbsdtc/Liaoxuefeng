#绑定属性时，如果直接把属性暴露，没法检查参数

#为了显示score范围，通过set_score()设置分数
#get_score()获取成绩，这样在set_score()方法里
#就可以检查参数

class Student(object):

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must be 0~100")
        self._score = value

    def get_score(self):
        return self._score


class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must be 0~100")
        self._score = value

s = Student2()
s.score = 60
print(s.score)
s.score = 9999
