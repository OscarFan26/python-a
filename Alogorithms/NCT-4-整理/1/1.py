# encoding: utf-8 #
"""
==========
File Name:              1                    
Author:                 Oscar Fan
Date:                   2022/4/7
requirements:                         
==========
"""
# （1）随机生成10个整数（范围在0到100，包含0和100），并且输出到控制台上。
#
# （2）编写快速排序算法，使得随机生成的十个数按照从大到小的顺序排序，并且输出到控制台。
#
# （3）编写快速排序算法，使得随机生成的十个数按照从小到大的顺序排序，并且输出到控制台。
import random


def fast_Sort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[-1]
		smaller = [x for x in arr[:-1] if x < pivot]
		greater = [x for x in arr[:-1] if x > pivot]
		return fast_Sort(smaller) + [pivot] + fast_Sort(greater)


def fast_Sort_reverse(arr):
	# fast sort but reverse it
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[-1]
		smaller = [x for x in arr[:-1] if x > pivot]
		greater = [x for x in arr[:-1] if x < pivot]
		return fast_Sort_reverse(smaller) + [pivot] + fast_Sort_reverse(greater)


test = [random.randint(0, 101) for i in range(10)]
print(fast_Sort_reverse(test))
print(fast_Sort(test))
