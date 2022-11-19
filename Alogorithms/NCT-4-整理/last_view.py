# encoding: utf-8 #
"""
==========
File Name:              last_view                    
Author:                 Oscar Fan
Date:                   2022/4/17
requirements:                         
==========
"""


# 冒泡排序
def bubble(alist: list):
	for i in range(len(alist)):
		for j in range(len(alist) - 1 - i):
			if alist[j] > alist[j + 1]:
				alist[j], alist[j + 1] = alist[j + 1], alist[j]
	return alist


def selection(alist: list):
	for i in range(len(alist) - 1, 0, -1):
		min_index = 0
		for j in range(1, i + 1):
			if alist[min_index] < alist[j]:
				alist[min_index], alist[j] = alist[j], alist[min_index]
		alist[i], alist[min_index] = alist[min_index], alist[i]
	return alist


def fast(alist: list):
	if len(alist) < 2:
		return alist
	else:
		pivot = alist[0]
		left = [x for x in alist[1:] if x <= pivot]
		right = [x for x in alist[1:] if x > pivot]
		return fast(left) + [pivot] + fast(right)


def insert(alist: list):
	for i in range(1, len(alist)):
		j = i
		while j > 0 and alist[j] < alist[j - 1]:
			alist[j], alist[j - 1] = alist[j - 1], alist[j]
			j -= 1
	return alist


def split(alist: list):
	n = len(alist)
	if n > 0:
		mid = n // 2
		if alist[mid] < 26:
			split(alist[:mid])
		elif alist[mid] > 26:
			split(alist[mid + 1:])
		else:
			return 1
