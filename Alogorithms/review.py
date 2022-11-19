# encoding: utf-8 #
"""
==========
File Name:              review                    
Author:                 Oscar Fan
Date:                   2022/4/13
requirements:  Github Copilot
==========
"""


# bubble sort
def bubble_sort(alist):
	for i in range(len(alist) - 1, 0, -1):
		for j in range(i):
			if alist[j] > alist[j + 1]:
				alist[j], alist[j + 1] = alist[j + 1], alist[j]
	return alist


# selection sort
def selection_sort(alist):
	for i in range(len(alist) - 1, 0, -1):
		max_index = 0
		for j in range(1, i + 1):
			if alist[j] > alist[max_index]:
				max_index = j
		alist[i], alist[max_index] = alist[max_index], alist[i]
	return alist


# insertion sort
def insertion_sort(alist):
	for i in range(1, len(alist)):
		j = i
		while j > 0 and alist[j] < alist[j - 1]:
			alist[j], alist[j - 1] = alist[j - 1], alist[j]
			j -= 1

	return alist


# fast sort
def fast_sort(alist):
	if len(alist) < 2:
		return alist
	else:
		pivot = alist[0]
		less = [i for i in alist[1:] if i <= pivot]
		greater = [i for i in alist[1:] if i > pivot]
		return fast_sort(less) + [pivot] + fast_sort(greater)


#  test these algorithms
if __name__ == '__main__':
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	print(bubble_sort(li))
	print(selection_sort(li))
	print(insertion_sort(li))
	print(fast_sort(li))
