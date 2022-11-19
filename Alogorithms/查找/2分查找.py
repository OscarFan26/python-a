# encoding: utf-8 #
"""
==========
File Name:              2分查找                    
Author:                 Oscar Fan
Date:                   2021/11/14
                        
==========
"""
import random
import sys

li = [random.randint(1, 100) for i in range(100)]
li.sort()
target = 26

lk = 0
hk = len(li) - 1

while lk <= hk - 1:
	mid = (lk + hk) // 2
	if target == li[mid]:
		print('get it. on index => {}'.format(li.index(target)))
		sys.exit()
	elif target > li[mid]:
		hk = mid + 1
	elif target < li[mid]:
		lk = mid - 1
