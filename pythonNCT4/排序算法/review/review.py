# encoding: utf-8 #
"""
==========
File Name:              review                    
Author:                 Oscar Fan
Date:                   2022/3/31
requirements:                         
==========
"""
import random


def bubbles(target: list):
    for i in range(1, len(target)):
        for j in range(len(target)-1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
    return target


def pi(arr: list, low: int, high: int):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return 1 + i


def fast(target: list, low: int, high: int):
    high -= 1
    if low < high:
        p = pi(target, low, high)
        fast(target, low, p-1)
        fast(target, p+1, high)
    return target


def insert(target: list):
    for i in range(1, len(target)):
        save = target[i]
        j = i
        while j > 0 and target[j-1] > save:
            target[j] = target[j - 1]
            j -= 1
        target[j] = save
    return target


def choice(target: list):
    for i in range(len(target)-1):
        min_index = i
        for j in range(1+i, len(target)):
            if target[j] < target[min_index]:
                min_index = j
        if i != target[min_index]:
            target[min_index], target[i] = target[i], target[min_index]
    return target


random_list = [random.randint(0, 10) for i in range(10)]
print('test numbers are: %s' % random_list)
print('bubbles: {}'.format(bubbles(random_list)))
print('fast: {}'.format(fast(random_list, 0, len(random_list))))
print('insert: {}'.format(insert(random_list)))
print('choice: {}'.format(choice(random_list)))
