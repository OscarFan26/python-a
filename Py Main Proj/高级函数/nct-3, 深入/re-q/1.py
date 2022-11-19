#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2021/8/21
# File name : 1
"""
字符串a = "not 404 found 张三 99 深圳"，
每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
"""
import re

s = "not 404 found 张三 99 深圳"

data = re.findall(r"[^a-zA-Z0-9 ]+", s)
for i in data:
    print(i, end=" ")
