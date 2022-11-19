# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/8/4 20:18
# Project name: solve.py
# IDE: PyCharm
# File name: 1.py
# 请你编写一个程序，用集合存储这两条观光路线的动物，路线A：大象，狮子，鳄鱼
# 海豚；路线B：狮子，老虎，鳄鱼，
# 并实现以下功能。
# （1）输入数字1：求出两个集合并集，并输出该集合。
# （2）输入数字2：求出两个集合交集，并输出该集合。
# 输入格式：
# 一个数字，1或者2
# 输出格式：
# 输出一个集合（集合内数据的顺序可不一致）
# 示例1
# 输入样例：
# 1
# 输出样例
# {"大象", "鳄鱼", "海豚","狮子", "老虎"}
# 示例2
# 输入样例：
# 2
# 输出样例
# {"鳄鱼","狮子"}
route_a = {"大象", "狮子", "鳄鱼", "海豚"}
route_b = {"狮子", "老虎", "鳄鱼"}
choice = input('>')

if choice == "1":
    print(route_a | route_b)
if choice == "2":
    print(route_a & route_b)
