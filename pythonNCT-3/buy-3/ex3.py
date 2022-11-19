# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/8/15 19:19
# Project name: solve.py
# IDE: PyCharm
# File name: ex3.py
# 请使用re库编写一个程序，输入一段包含数字的字符串，输出字符串中的数字。
#
# 输入格式
#
# 输入包含数字的字符串
#
# 输出格式
#
# 输出由字符串中的数字组成的列表
import re

a = input("enter str :>_>>")
find = re.findall(r"\d+", a)
print(find)
