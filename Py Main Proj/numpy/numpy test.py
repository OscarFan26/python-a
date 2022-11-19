# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/8/14 14:44
# Project name: nct lv1.py
# IDE: PyCharm
# File name: numpy test.py
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("this array's data type is", array.dtype)
print("this array's shape is", array.shape)
print("this array's type is", type(array))
# ---------- shape ---------------- #
print("# ---------- shape ---------------- #")
typenp = np.dtype("i4")
ndarray = np.array([[[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]], dtype=typenp)

print('this ndarray\'s shape is', ndarray.shape)
print("this ~ data type is", ndarray.dtype)
# create new
print('-*- create new -*-')
xxx = np.empty([1, 2, 3, 5, 6], dtype=int)
yyy = np.ones([6, 6, 9], dtype=int)
zzz = np.zeros([2, 3, 4], dtype=float)
print(xxx)
print(yyy)
print(zzz)
print(xxx.dtype, yyy.dtype, zzz.dtype)
print(type(xxx), type(yyy), type(zzz))
