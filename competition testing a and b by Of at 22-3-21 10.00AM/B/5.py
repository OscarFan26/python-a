# encoding: utf-8 #
"""
==========
File Name:              5                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:                         
==========
"""

# 就简单到离谱，根本无法比得上 冒泡 和 快速 排序算法
# 给你一个整数 x ，如果 x 是一个回文整数，输出 true ；否则，输出 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是.
targ_num = str(input())  # 输入，必须以字符串格式输入，不然后面不好切分
tell_you_when_to_stop = True  # 字面意思，就是变量长了点...
times = int(len(targ_num) / 2)  # key key key!
count = 0
while tell_you_when_to_stop and count != len(targ_num):
	tell_you_when_to_stop = targ_num[count] == targ_num[-1 - count]
	count += 1
if tell_you_when_to_stop:  # 不得不说，我写的这判断条件太tm神奇了
	print('true')
else:
	print('false')
