#!/usr/bin/python

class people:
    name = ''
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def show():
        print("%s says: I'm %d years old"%(self.name, self.age))

class student(people):
    def __init__(self, name, age, weight, grade):
        #调用父类构造函数
        people.__init__(self, name, age, weight)
        self.grade = grade

    #覆写父类方法
    def show(self):
        print("%s says: I'm %d years old, and I'm in grade %d, my weight is %d"%(self.name, self.age, self.grade, \
        self.weight))


s = student('tatumn', 10, 60, 3 )
print('name:', s.name)
s.show()

