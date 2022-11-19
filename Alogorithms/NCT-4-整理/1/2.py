# encoding: utf-8 #
"""
==========
File Name:              2                    
Author:                 Oscar Fan
Date:                   2022/4/7
requirements:                         
==========
"""
# （1）随机生成10个整数（范围在0到100，包含0和100），并且输出到控制台上。
#
# （2）编写冒泡排序算法，使得随机生成的十个数按照从大到小的顺序排序，并且输出到控制台。
#
# （3）编写二分查找算法，判断30个数字中是否存在数字10，如果存在，输出10在这30个整数中出现的第一个位置，如果不存在，输出“这些数字中没有10”。
import random, sys


def bubble_sort(arr: list):
	for i in range(len(arr)):
		for j in range(len(arr) - i - 1):
			if arr[j] < arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr


def split_search(arr: list):
	n = len(arr)
	if n > 0:
		mid = n // 2
		if arr[mid] < 10:
			return split_search(arr[:mid])
		elif arr[mid] > 10:
			return split_search(arr[mid + 1:])
		else:
			return 10


test = [random.randint(0, 100) for i in range(10)]
# test = [57, 74, 84, 1, 32, 10, 36, 31, 38, 21]
print(test)
print(bubble_sort(test))
returns = split_search(bubble_sort(test))
# returns = split_search(bubble_sort([1,2,3,4,5,6,7,8,9,10]))
if returns == 10:
	print(10)
else:
	print("这些数字中没有10")
# print(returns)
