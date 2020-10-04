#!/usr/bin/python

class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Str: user:%s age:%d"%(self.name, self.age)

    def __repr__(self):
        return "an user:%s age:%d "%(self.name, self.age)

#打印User类对象
user = User('ryan', 20)
print(user) # print 会调用对象的__str__方法.


'''
如果没有添加__str__方法，而python又需要该方法时，它会去调用__repr__方法。

__str__ 和 __repr__的区别：
前者，可读性强，便于阅读；
后者，显示的更准确，主要用于调试，便于开发者使用。
'''