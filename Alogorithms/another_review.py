import random


# 在这个文件里，我将打出5个不同的算法（4个排序算法和1个查找算法）
# Let's get started!

def bubble_sort(alist):
	"""
	冒泡排序
	"""
	for passnum in range(len(alist) - 1, 0, -1):
		for i in range(passnum):
			if alist[i] > alist[i + 1]:
				alist[i], alist[i + 1] = alist[i + 1], alist[i]
	return alist


def selection_sort(alist):
	"""
	选择排序
	"""
	for fillnum in range(len(alist) - 1, 0, -1):
		maxpos = 0
		for location in range(1, fillnum + 1):
			if alist[location] > alist[maxpos]:
				maxpos = location
		alist[fillnum], alist[maxpos] = alist[maxpos], alist[fillnum]
	return alist


def insertion_sort(alist):
	"""
	插入排序
	"""
	for index in range(1, len(alist)):
		currentvalue = alist[index]
		position = index
		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position -= 1
		alist[position] = currentvalue
	return alist


def fast_sort(alist):
	"""
	快速排序
	"""
	if len(alist) <= 1:
		return alist
	else:
		pivot = alist[0]
		less = [i for i in alist[1:] if i <= pivot]
		greater = [i for i in alist[1:] if i > pivot]
		return fast_sort(less) + [pivot] + fast_sort(greater)

	# 二分查找 -- 递归性


def binary_search(alist, item):
	if len(alist) == 0:
		return False
	else:
		mid = len(alist) // 2
		if alist[mid] == item:
			return True
		elif alist[mid] > item:
			return binary_search(alist[:mid], item)
		else:
			return binary_search(alist[mid + 1:], item)


# so let's get started~
# TEST THEM
if __name__ == "main":
	test_list = [random.randint(0, 100) for i in range(10)]
	print(test_list)
	print(bubble_sort(test_list))
	print(selection_sort(test_list))
	print(insertion_sort(test_list))
	print(fast_sort(test_list))
	print(binary_search(test_list, 26))
