# -*- encoding = utf-8 -*-
# Author: pc
# Create Time: 2021/4/10 19:53
# Project name: nct lv1.py
# IDE: PyCharm
# File name: 所有开头的数字内容或数字.py
# 匹配一行文字中的开头的数字或文字
import re


def start_num_or_letter(put_in):
    a = re.match("[0-9a-zA-Z]*", put_in)
    if a.group():
        print("input:", put_in)
        print("match result:", a.group())
    else:
        print("error match.")


ask = input("enter sth\n>>>")
start_num_or_letter(ask)
