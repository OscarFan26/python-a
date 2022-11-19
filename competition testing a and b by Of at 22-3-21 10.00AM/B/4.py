# encoding: utf-8 #
"""
==========
File Name:              4                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:                         
==========
"""
# 定义一个函数sort_list（），功能为将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。即输入为两个升序列表，输出为合并后的升序列表
# 比如：输入：l1 = [1,2,4], l2 = [1,3,4]输出：[1,1,2,3,4,4]


# 不是，如果你连这么简单的题都不会，你可能真的是一个**了
li1: list = eval(input())  # 输入啊。。。
li2: list = eval(input())
answer_li = []
temp_li = list(zip(li1, li2))  # zip一起啊
for i in range(len(temp_li)):
	for j in range(2):
		answer_li.append(temp_li[i][j])  # 加进来啊。。。
print(answer_li)  # 输出啊
