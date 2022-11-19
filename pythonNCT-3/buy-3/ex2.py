# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/8/15 19:16
# Project name: solve.py
# IDE: PyCharm
# File name: ex2.py
#  请编写一个程序，创建字典存储语文、数学、英语三科学科分数，
#  程序运行后用户输入三个分数（用空格隔开），
#  将三个分数依次保存到字典中，最终将字典打印出来。
#
# 输入格式
#
# 输入三个分数（用空格隔开）
#
# 输出格式
#
# 输出一个字典，分别存储语文、数学、英语三科分数
a = input("enter marks >>>")
marks = [i for i in a.split(' ')]
dic = {"语文": marks[0], "数学": marks[1], "英语": marks[2]}
print(dic)
