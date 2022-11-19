# encoding: utf-8 #
"""
==========
File Name:              选择                    
Author:                 Oscar Fan
Date:                   2022/3/24
requirements:                         
==========
"""
import random


def 选择(arr: list):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != arr[min_index]:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


random_list = [random.randint(0, 100) for i in range(5)]
print('The random list is: {}'.format(random_list))
print('Which the output is {}'.format(选择(random_list)))
