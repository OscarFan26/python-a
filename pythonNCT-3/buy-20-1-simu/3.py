# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/8/4 20:32
# Project name: solve.py
# IDE: PyCharm
# File name: 3.py
# 程老师需要把下面表格中的数据进行处理，请按照下列要求完成程序。
#
# （1）输入对应的数字，生成下列表格
#
# 姓名  身高  体重
#  小本  43kg  1.48米
#  小辰  38kg 1.49米
# 输入格式：
#
# 请输入小本的身高和体重数字，用英文逗号隔开：43,1.48
#
# 请输入小辰的身高和体重数字，用英文逗号隔开：38,1.49
#
# （2）发现记录学生的表格出现了问题，体重和身高的数据填入相反，
# 现在需要把该csv文件中身高数据和体重数据对换。
import csv

ben = input('请输入小本的身高和体重数字，用英文逗号隔开：')
ceng = input('请输入小辰的身高和体重数字，用英文逗号隔开：')
l1 = [i for i in ben.split(',')]
l2 = [j for j in ceng.split(',')]
dict1 = [{"姓名": "小本", "身高": l1[1]+"米", "体重": l1[0]+"kg"},
         {"姓名": "小辰", "身高": l2[1]+"米", "体重": l2[0]+"kg"}]

with open('data1.csv', 'a+', encoding="utf-8") as fp:
    writer = csv.DictWriter(fp, ["姓名", "身高", "体重"])
    writer.writeheader()
    writer.writerows(dict1)
