# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/8/15 19:13
# Project name: solve.py
# IDE: PyCharm
# File name: ex1.py
# 请编写一个程序，输入任意一段字符串，将字符串转换为集合后，判断其中是否有小写字符串'a'
# 如果有则将小写a删除，其他元素均不改变，输出集合最终的结果。
#
# 输入格式
#
# 输入一段任意字符串
#
# 输出格式
#
# 输出一个集合，将其中的小写a删除，其他元素不变（元素顺序无关）
#
a = input("enter >>>")
set1 = set(a)
if 'a' in set1:
    set1.remove('a')
print(set1)
