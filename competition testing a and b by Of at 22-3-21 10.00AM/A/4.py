# encoding: utf-8 #
"""
==========
File Name:              4                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:                         
==========
"""
# 4、给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值的那两个整数,nums指定为：[2,7,11,15],target为用户手动输入。如果nums中找不到两个整数相加的和等于target,则输出不存在。
# 示例：输入target=9，则输出2，7

# 解：一个小算法，不必紧张
# 算法 -> 函数 -> 调用他 -> 输出
# 关键是理解题目：这里指的是列表中任何的两个树
# 怀疑抄LEETCODE,只是把他翻译成中文而已
nums = [2, 7, 11, 15]
target = int(input())  # int int int!


def search(dest: list, search: int):
	for i in dest:  # 两行代码
		for j in dest:  # 双重循环， 快乐多多
			if j != i and i + j == search:
				return i, j


p1, p2 = search(nums, target)  # 解包他
print(f'{p1}，{p2}')
