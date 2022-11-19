#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2021/8/21
# File name : 3
"""
输出一个集合，将其中的小写a删除，其他元素不变（元素顺序无关）
"""
a = set(input("set>"))
if "a" in a:
    a.remove("a")
print(a)
