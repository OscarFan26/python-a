# encoding: utf-8 #
"""
==========
File Name:              2                    
Author:                 Oscar Fan
Date:                   2022/4/14
requirements:                         
==========
"""
import random


def fast_sort(alist):
	if len(alist) < 2:
		return alist
	else:
		pivot = alist[0]
		less = [i for i in alist[1:] if i >= pivot]
		greater = [i for i in alist[1:] if i < pivot]
		return fast_sort(less) + [pivot] + fast_sort(greater)


def split_search(arr: list):
	n = len(arr)
	if n == 0:
		return arr
	else:
		mid = n // 2
		if arr[mid] < 23:
			return split_search(arr[:mid])
		elif arr[mid] > 23:
			return split_search(arr[mid + 1:])
		else:
			return "ok"


li = [random.randint(0, 51) for i in range(10)]
print(li)
li = fast_sort(li)
print(li)
if split_search(li) == "ok":
	print(23)
else:
	print("这些数字中没有23")
