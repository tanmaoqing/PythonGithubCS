"""
=====================
Author：Tan
Time：2023/2/24 16:44
Project：python学习
=====================
"""


class Test:
    def __int__(self, name, age, sex):
        self.my_name = name
        self.my_age = age
        self.my_sex = sex
        self.my_eat = "chi"

    def test_name(self, eat):
        print("吃{}".format(eat))
        self.my_name = "小任"
        print(self.my_name)
        self.my_eat = eat

    def test_mm(self):
        pass
