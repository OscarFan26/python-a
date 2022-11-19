# encoding: utf-8 #
"""
==========
File Name:              3                    
Author:                 Oscar Fan
Date:                   2022/3/31
requirements:                         
==========
"""
"""
请运用队列相关的知识编写程序，模拟银行排号系统。

1. 创建一个队列类，队列类中有入队、出队、返回队列中元素数量三个方法；

2. 实例化该队列，模拟排号系统的功能，功能如下：

（1）输入数字1，可以新增顾客序号，将顾客序号添加到队列里（即入队操作），并打印此时队列中的元素；

（2）输入数字2，可以删除处理完业务的顾客序号（即出队操作），并打印此时队列中的元素，若队列中元素数量为0时，不可以执行删除操作；

（3）输入数字3，退出程序。
"""


class Queue:
	def __init__(self):
		self.queue = []

	def enter(self, num):
		self.queue.insert(0, num)

	def leave(self):
		if len(self.queue) != 0:
			self.queue.pop(0)


queue = Queue()
while True:
	ask = int(input())
	if ask == 3:
		break
	elif ask == 1:
		num = input()
		queue.enter(num)
		print(queue.queue)
	elif ask == 2:
		queue.leave()
		print(queue.queue)
	else:
		pass
