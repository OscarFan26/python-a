# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/7/28 18:45
# Project name: pythonNCT-3
# IDE: PyCharm
# File name: ce.py
#
# 中国、美国、韩国、日本、新加坡、德国、英国
country_str = '中国、美国、韩国、日本、新加坡、德国、英国'
country_list = [country+',' for country in country_str.split('、')]
country_list[-1] = '英国'
for info in country_list:
    print(info, end='')
