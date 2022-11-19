#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2021/8/21
# File name : 2
"""
请使用re库编写一个程序，输入一段包含数字的字符串，输出字符串中的数字。
输入格式
输入包含数字的字符串
输出格式
输出由字符串中的数字组成的列表
示例1
输入样例
ab12cd34ef56
输出样例
['12', '34', '56']
"""
import re

a = input("str>")

data = re.findall(r"[0-9]+", a)
print(data)