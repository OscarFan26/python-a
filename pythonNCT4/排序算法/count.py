# encoding: utf-8 #
"""
==========
File Name:              count                    
Author:                 Oscar Fan
Date:                   2022/3/24
requirements:                         
==========
"""
import random


def count(arr: list):
    max_n = max(arr)
    answer = []
    count = [0 for i in range(max_n)]
    for i in arr:
        for j in range(1, max_n+1):
            if i == j:
                count[j-1] += 1
    for i in range(len(count)):
        if count[i]:
            for j in range(count[i]):
                answer.append(i+1)
    return answer


random_list = [random.randint(0, 100) for i in range(10)]
print('The random list is: {}'.format(random_list))
print('Which the output is {}'.format(count(random_list)))

