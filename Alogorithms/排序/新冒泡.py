# encoding: utf-8 #
"""
==========
File Name:              新冒泡                    
Author:                 Oscar Fan
Date:                   2021/10/23
                        
==========
"""
from copy import deepcopy
import random
import time

# 生成随机数字
# li = [random.randint(1, 100) for y in range(30)]
#
#
# listset = deepcopy(li)
# listset.sort()
#
# # 冒泡开始
# print('原来随机生成的列表是:{}'.format(li), '\n\n')
li = [1, 3, 4, 2, 5, 7, 6]
times = time.time()
for i in range(len(li)):
	for j in range(len(li) - i - 1):
		if li[j] > li[j + 1]:
			li[j], li[j + 1] = li[j + 1], li[j]
			print('exchanged {} and {}.\n\n'.format(li[j], li[j + 1]))
		else:
			print('pass {} or {}\n'.format(j, j + 1))
print('现在列表是: {}'.format(li))
print('用了 {} 秒'.format(time.time() - times))
