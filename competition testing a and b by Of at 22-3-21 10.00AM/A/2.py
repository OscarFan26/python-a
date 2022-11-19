# encoding: utf-8 #
"""
==========
File Name:              2                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:           Py 3.9
==========
"""


#  编写一个接受句子并计算字母和数字的程序。假设为程序提供了以下输入：
# 	Hello world! 123
# 	然后，输出应该是：字母10	数字3


def Count(target: str):
	letters = 0
	numbers = 0
	for i in target:
		if 'A' <= i <= 'Z' or 'a' <= i <= 'z':  # 用ASCII比大小
			letters += 1  # 这种方法来自c/c++
		elif '0' <= i <= '9':
			numbers += 1
	return letters, numbers


target = input()
letters, numbers = Count(target)  # 解包函数
print(f'字母{letters} 数字{numbers}')
