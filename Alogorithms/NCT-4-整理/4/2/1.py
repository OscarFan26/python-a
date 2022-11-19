# encoding: utf-8 #
"""
==========
File Name:              1                    
Author:                 Oscar Fan
Date:                   2022/4/14
requirements:                         
==========
"""
import random


def bubble_sort(arr: list):
	for i in range(len(arr)):
		for j in range(len(arr) - 1 - i):
			if arr[j] < arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr


li = [random.randint(0, 1001) / 100 for _ in range(10)]
print(li)
print(bubble_sort(li))
