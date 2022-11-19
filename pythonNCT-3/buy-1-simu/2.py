# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/8/1 20:18
# Project name: pythonNCT-3
# IDE: PyCharm
# File name: 2.py
# 编写一个程序，输入一串字符a和一串数字b，相邻字符或数字使用英文逗号“,”隔开，
# 字符串a的字符做为字典的键（键为字符串），数字串b中的数字做为字典的值（值为数字），
# 输出字典中所有值的和。
#
# 输入样例：
# a,b,c,d
# 1,2,3,4
#
# 输出：
# 10
def func(my_dict):
    sum = 0
    for i in my_dict:
        sum = sum + my_dict[i]
    return sum


a = input()
list1 = a.split(',')
b = input()
list2 = b.split(',')
list3 = [int(i) for i in list2]
dict1 = dict(zip(list1, list3))
print(func(dict1))
