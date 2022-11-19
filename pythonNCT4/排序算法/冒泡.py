# encoding: utf-8 #
"""
==========
File Name:              冒泡                    
Author:                 Oscar Fan
Date:                   2022/3/24
requirements:                         
==========
"""
import random


def 冒泡(arr: list):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print('The random list is: {}'.format(random_list))
print('Which the output is {}'.format(冒泡(random_list)))
