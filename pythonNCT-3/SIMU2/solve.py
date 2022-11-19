# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/7/31 18:30
# Project name: pythonNCT-3
# IDE: PyCharm
# File name: solve.py
# 根据下面一个字符串（可以直接复制到代码），对其进行二维数据格式化输出。
#
# 字符串：
#
# 年级, 姓名, 性别, 身高, 年龄\n1, 小明, 男, 168, 23\n1,
# 小红, 女, 162, 22\n2, 小张, 女, 163, 21\n2, 小丽, 男, 158, 21\n
str1 = "年级, 姓名, 性别, 身高, 年龄\n1, 小明, 男, 168, 23\n1, 小红, " \
       "女, 162, 22\n2, 小张, 女, 163, 21\n2, 小丽, 男, 158, 21\n"
ls = [str1.strip('\n').split(',')]
for row in ls:
    line = ''
    for item in row:
        line += "{}\t".format(item)
    print(line)
