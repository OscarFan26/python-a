# encoding: utf-8 #
"""
==========
File Name:              1                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:                         
==========
"""

# 编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，1000至2021(包括在内)，输出这些数字并统计满足条件的数字的个数。
count = sum(i % 7 == 0 and i % 5 != 0 for i in range(1000, 2022))
print(count)
