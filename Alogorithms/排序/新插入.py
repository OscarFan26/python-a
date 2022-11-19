# encoding: utf-8 #
"""
==========
File Name:              新插入                    
Author:                 Oscar Fan
Date:                   2021/10/26
                        
==========
"""
import random
import time
from copy import deepcopy

timenow = time.time()

l_sort = [random.randint(1, 99) for xx in range(30)]
l = deepcopy(l_sort)

for i in range(len(l)):
	for j in range(i, 0, -1):
		if l[j] < l[j - 1]:
			l[j], l[j - 1] = l[j - 1], l[j]
		else:
			break

print("list is: {}".format(l))
print("time cost: {}".format(time.time() - timenow))
