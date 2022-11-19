# encoding: utf-8 #
"""
==========
File Name:              main                    
Author:                 Oscar Fan
Date:                   7/21/2022
requirements:                         
==========
"""
"""
[可迭代对象 [
	迭代器 [
		生成器
		]
	]
]
"""

# iter
# for _ in iter
# str, seq...
import typing
# from collections import Iterator
# from collections import Iterable
x = [1, 2, 3]
y = iter(x)
z = iter(x)
print(next(y))
print(next(y))
print(next(z))
print(type(x), type(y))
print(next(y))
try:
	print(next(y))
except StopIteration:
	print('StopIteration')

# 可以被for-loop的obj都是Iterable
# 可以next()的对象都是Iterable, 他们表示一个惰性计算的序列
# seq是Iterable, 不是Iterator, 但可以通过iter()得到一个Iterator obj
