# encoding: utf-8 #
"""
==========
File Name:              插入排序                    
Author:                 Oscar Fan
Date:                   2021/10/23
                        
==========
"""
from copy import deepcopy
import random
import time

# 生成随机数字
li = [random.randint(1, 100) for y in range(30)]

listset = deepcopy(li)
listset.sort()

# 冒泡开始
print('原来随机生成的列表是:{}'.format(li), '\n\n')

times = time.time()
for i in range(1, len(li)):
	key = li[i]
	j = i - 1
	while j >= 0 and key < li[j]:
		li[j + 1] = li[j]
		print('exchange {} and {}'.format(li[j + 1],
		                                  li[j]))
		j -= 1
		print('fine.ok.\n')
	li[j + 1] = key

print('list is:', li)
print('time:', time.time() - times)
