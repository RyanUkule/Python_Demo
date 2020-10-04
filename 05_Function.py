#!/usr/bin/python

# 函数说明：验证不可变类型的参数
def Test_number(num):
    num = num + 1
    print('tem num:', num)
    return

# 函数调用
num = 1
Test_number(num)
print('num:', num)

'''
函数参数类型：
1.必须参数
2.关键字参数
3.默认参数
4.不定长参数（*：tuple, **: dict）
'''