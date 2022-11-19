# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/7/28 17:59
# Project name: pythonNCT-3
# IDE: PyCharm
# File name: ci.py
#
str_in = str(input('enter >  '))
num_in = input('enter another 》》')

a_dict_new = {}
init = 0

key_str = [key for key in str_in.split(',')]
value_num = [int(value) for value in num_in.split(',')]

for k in key_str:
    for n in value_num:
        a_dict_new[k] = n

for a_dict in a_dict_new.values():
    int(a_dict)
    init = 0
    if a_dict > init:
        init = a_dict
    else:
        pass

print(init)
