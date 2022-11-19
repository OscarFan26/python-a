# encoding: utf-8 #
"""
==========
File Name:              选择排序                    
Author:                 Oscar Fan
Date:                   2021/10/23
                        
==========
"""
from copy import deepcopy
import random
import time

l1 = [random.randint(1, 100) for y in range(30)]

listset = deepcopy(l1)
listset.sort()

# 冒泡开始
print('原来随机生成的列表是:{}'.format(l1), '\n\n')
timenow = time.time()
for i in range(len(l1)):
	min_index = i
	for j in range(i + 1, len(l1)):
		if l1[min_index] > l1[j]:
			min_index = j
		else:
			print('pass {} and {}\t'.format(l1[min_index], l1[j]))
	l1[min_index], l1[i] = l1[i], l1[min_index]
	print('exchange {} and {}\n'.format(l1[min_index], l1[j]))

print('排序后列表: {}'.format(l1))
print('用时:{}'.format(time.time() - timenow))
