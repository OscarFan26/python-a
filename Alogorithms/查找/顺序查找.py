# encoding: utf-8 #
"""
==========
File Name:              顺序查找                    
Author:                 Oscar Fan
Date:                   2021/11/14
                        
==========
"""
import random
import sys

l = [random.randint(1, 100) for i in range(30)]


def find(li: list, target: int):
	for i in range(len(li)):
		if target == li[i]:
			print('get it, on index {}'.format(i))
			sys.exit()

	print('no target in list')


target = input('target ==> ')
find(l, int(target))
