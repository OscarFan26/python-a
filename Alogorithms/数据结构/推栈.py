# encoding: utf-8 #
"""
==========
File Name:              推栈
Author:                 Oscar Fan
Date:                   2021/10/23

==========
"""


class Stack:
	def __init__(self):
		self.stack = []
		self.limit = 100
		self.len = 0

	def append(self, name):
		if self.len == self.limit:
			print('FULL, fail to append')
		else:
			self.stack.append(name)
			self.len += 1
			print('append --ok')
			self.pop()

	def pop(self):
		if self.len == 0:
			print('EMPTY, fail to pop ')
		else:
			self.stack.pop(0)
			self.len -= 1
			print('pop --ok')


a = Stack()
for i in range(300):
	a.append(i)
print(a.stack)
