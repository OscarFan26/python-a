# encoding: utf-8 #
"""
==========
File Name:              插入                    
Author:                 Oscar Fan
Date:                   2022/3/24
requirements:                         
==========
"""
import random


def 插入(arr: list):
    for i in range(len(arr)):
        current = i
        while current > 0 and arr[current] < arr[current - 1]:
            arr[current], arr[current - 1] = arr[current - 1], arr[current]
            current -= 1
    return arr

# 插入排序




# random_list = [random.randint(0, 100) for i in range(10)]
# print('The random list is: {}'.format(random_list))
# print('Which the output is {}'.format(插入(random_list)))
