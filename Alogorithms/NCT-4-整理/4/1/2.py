# encoding: utf-8 #
"""
==========
File Name:              2                    
Author:                 Oscar Fan
Date:                   2022/3/31
requirements:                         
==========
"""
"""
请运用栈相关的知识编写一个程序，满足以下要求。

1. 创建栈类，使栈类具有出栈、入栈两个个方法；

2. 使用创建的栈类，用户输入一串数字用逗号隔开，将隔开的数字依次入栈，最后打印出栈的顺序

输入格式：

一串数字用逗号隔开

输出格式：

一串数字用逗号隔开
"""


class Stack:
	def __init__(self):
		self.stack = []

	def insert(self, num):
		self.stack.insert(0, num)

	def pop(self):
		if len(self.stack) == 1:
			print(self.stack[0], end='')
		else:
			print(self.stack[0], end=",")
		self.stack.pop(0)


stack = Stack()
some_num = input().split(',')
for i in some_num:
	stack.insert(i)
for j in range(len(some_num)):
	stack.pop()
