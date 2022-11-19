# encoding: utf-8 #
"""
==========
File Name:              快速                    
Author:                 Oscar Fan
Date:                   2022/3/24
requirements:                         
==========
"""
import random


def fast(arr: list, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return 1+i


def sort_quick(arr, low, high):
    if low < high:
        pi = fast(arr, low, high)
        sort_quick(arr, low, pi-1)
        sort_quick(arr, pi+1, high)
    return arr


random_list = [random.randint(1, 10) for i in range(10)]
print('The random list is: {}'.format(random_list))
print('Which the output is {}'.format(sort_quick(random_list, 0, len(random_list)-1)))
