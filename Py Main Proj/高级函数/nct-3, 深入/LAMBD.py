#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2021/8/21
# File name : LAMBDA
"""
Lambda: 匿名函数
lambda parameter: expression
return: func obj
"""


# Caution
# 1. No more expression.
# 2. No exec in <lambda>.
# lambda x, y, z: (x)(y)(z)


def a():
    pass


print(a)
print(lambda x: x ** 2)  # <function <lambda> at 0x00000187B4F321F0>
