# encoding: utf-8 #
"""
==========
File Name:              3                    
Author:                 Oscar Fan
Date:                   2022/4/7
requirements:                         
==========
"""


# 编写代码实现一个队列 Queue类 ，使其具备入队、出队的功能，实例化后分别进行元素 'a' 入队、元素 'b' 入队、出队、元素 'd' 入队、出队、元素 'e' 入队操作，最后将队列的结果打印出来。


class Queue:
	def __init__(self):
		self.queue = []

	def insert(self, data):
		self.queue.append(data)

	def delete(self):
		self.queue.pop(0)


queue = Queue()
queue.insert('a')
queue.insert('b')
queue.delete()
queue.insert('d')
queue.delete()
queue.insert('e')
print(queue.queue)
