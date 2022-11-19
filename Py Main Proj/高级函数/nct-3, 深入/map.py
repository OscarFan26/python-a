#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2021/8/21
# File name : map
"""
map(func, Iter[])
...^^^^^ +=> |||
"""
# map
print(list(map(lambda x: x ** 2, [i for i in range(1, 101)])))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256,
# ... ]
