#!/usr/bin/python
#-*- UTF-8 -*-

#斐波那契数列
a, b = 0, 1
while b< 10:
	print(b, end=',')
	a, b = b, a + b

