#!/usr/bin/env python
#encoding=utf8


"""
面向对象示例
"""
class A:
    def __init__(self):
        self.name = 'A'

    def dosomething(self):
        # 多态
        print(self.someinfo())

    def someinfo(self):
        return "I am " + self.name


class B(A):
    def someinfo(self):
        # self.name继承自父类A
        return "My fathar class is " + self.name


class C(A):
    def someinfo(self):
        return "I'm Cool"


a = A()
b = B()
c = C()
a.dosomething()
b.dosomething()
c.dosomething()
