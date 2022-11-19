# encoding: utf-8 #
"""
==========
File Name:              队列
Author:                 Oscar Fan
Date:                   2021/11/6

==========
"""


class Queue:
	def __init__(self):
		self.queue = []
		self.is_null = False
		self.limit = 50
		self.is_full = False

	def push(self, push_name):
		if len(self.queue) == self.limit:
			print('Queue is FULL! Cannot push!!')
			pass
		else:
			self.queue.append(push_name)
			print('{} pushed'.format(push_name))

	def pop(self):
		if not self.queue:
			print('Queue is EMPTY! Cannot pop!!')
		else:
			pop = self.queue.pop(0)
			print('{} popped'.format(pop))


queue_a = Queue()
for i in range(100):
	queue_a.push(i)
print(queue_a.queue)
print('\n\n\n\t\n\n\n\t\n')
for j in range(300):
	queue_a.pop()
print(queue_a.queue)
