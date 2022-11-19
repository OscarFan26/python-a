# -*- encoding = utf-8 -*-
# Author: pc
# Create Time: 2021/4/10 19:40
# Project name: nct lv1.py
# IDE: PyCharm
# File name: 所有开头字母.py
import re

def if_letter(put_in):
    a = re.match("[a-zA-Z]*", put_in)
    if a.group():
        print("input:", put_in)
        print("match result:", a.group())
    else:
        print("error match:", put_in)


ask = input("enter sth \n>>>")
if_letter(ask)
