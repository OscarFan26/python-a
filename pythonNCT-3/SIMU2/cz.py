# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/7/28 18:16
# Project name: pythonNCT-3
# IDE: PyCharm
# File name: cz.py
#
#  小明编写了一个程序，该程序能够实现判断输入的数字串是否正确。数字段要满足要求如下：
#
# （1）输入一组数字，判断数字串是否为11位数字；
#
# （2）前两位数字为13，第三位数字为4-9之间任意数字，第4位到11位数字位任意数字；
#
# （3）若该数字串满足上述要求，输出1，不满足，输出0。
import re

input_ = str(input('enter 11 numbers please >>>'))
pattern = re.compile(r'^13[^1230]\d{8}$')

if len(input_) == 11:
    m = pattern.match(input_).group()
    if m == input_:
        print(1)
else:
    print(0)
