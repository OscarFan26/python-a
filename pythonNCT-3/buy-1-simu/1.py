# -*- encoding: utf-8 -*-
# Author: Oscar
# Create Time: 2021/8/1 20:13
# Project name: pythonNCT-3
# IDE: PyCharm
# File name: 1.py
# 某学校组织学生报名课余兴趣班，兴趣班共有两门，分别是足球课和篮球课。
#
# 报足球课的学生有：
#
# 小明，小黄，小强，小熊，小武，小二
#
# 报篮球课的学生有：
#
# 大雄，小强，小慧，小杨，小明
#
# 请编写一个程序，将报名足球课和篮球课的学生姓名分别存储在两个集合中，
# 输出两个集合中重复的人名。
football = "小明，小黄，小强，小熊，小武，小二"
basketball = "大雄，小强，小慧，小杨，小明"
football = set([it_foot for it_foot in football.split('，')])
basketball = set([it_basketball for it_basketball in basketball.split('，')])
print(football & basketball)
