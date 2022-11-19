# encoding: utf-8 #
"""
==========
File Name:              all
Author:                 Oscar Fan
Date:                   2022/4/7
requirements:                         
==========
"""
import random
# We will review the four sorting algorithms at this py file
# Bubble Sort, Selection Sort, Insertion Sort, and Fast Sort
# Functions:
print("We will review the four sorting algorithms: Bubble Sort, Selection Sort, Insertion Sort, and Fast Sort\n")
print("At this Program\n")
print("-----------------------------------------------------\n")


def bubble_sort(alist):
    """
    Bubble Sort
    """
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist


def selection_sort(arr):
    #  from small to big, WARNING!!!!
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != arr[min_index]:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


#  fast sort last one using only one func
def fast_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]
        return fast_sort(left) + [pivot] + fast_sort(right)


#  Here we go, we're gonna test the four algorithms using
#  random, each random 10 nums range from 0 to 100 (including)
test = [random.randint(0, 100) for i in range(10)]
print("The original list is:", test)
print("------------------------------------------------------")
print("Bubble Sort:", bubble_sort(test))
print("Selection Sort:", selection_sort(test))
print("Insertion Sort:", insertion_sort(test))
print("Fast Sort:", fast_sort(test))
print("------------------------------------------------------")
