# encoding: utf-8 #
"""
==========
File Name:              冒泡实验
Description:                    
Author:                 Oscar Fan
Date:                   2021/9/25
                        
==========
"""
# 冒泡实验
from copy import deepcopy
import random
import time

# 生成随机数字
li = []
for i in range(30):
	num_random = random.randint(1, 100)
	li.append(num_random)

listset = deepcopy(li)
listset.sort()

# 冒泡开始
print('原来随机生成的列表是:{}'.format(li), '\n\n')

times = time.time()
while True:
	for sept in range(len(li) - 1):
		for sept2 in range(len(li) - 1 - sept):
			if li[sept2] > li[sept2 + 1]:
				li[sept2], li[sept2 + 1] = li[sept2 + 1], li[sept2]
				print('{} <---> {}\n...changing...OK'.format(li[sept2],
				                                             li[sept2 + 1]))
				print(li, '\n\n')
			else:
				if li[sept2] == li[sept2 + 1] or li[sept2] < li[sept2 + 1]:
					print(
						'em... pass {} and {}'.format(li[sept2], li[sept2 + 1]))

	if listset == li:
		break

print('现在列表是: {}'.format(str(li).strip('[').strip(']')), '\n')
print('用了 {} 秒'.format(time.time() - times))
