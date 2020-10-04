#!/usr/bin/python

#lambda表达式
sum = lambda arg1, arg2: arg1 + arg2

#调用sum函数
print('Sum:', sum(1, 2))


'''
1. Lambda 主体是一个表达式，而不是代码块，所以，只能封装有限的逻辑。
2. Lambda 拥有自己的命名空间，所以，不能访问自己参数列表之外 或 全局命名空间里的参数。

'''