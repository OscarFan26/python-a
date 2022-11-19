'''
OscarFan 制作 : 
Date: 2022-03-21 08:59:33
Have a good day forever~~~: ::python::cpp::js::html::css::bash???
'''
# encoding: utf-8 #
"""
==========
File Name:              5                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:                         
==========
"""


# 卡拉兹(Callatz)猜想：对任何一个正整数 n，如果它是偶数，那么把它砍掉一半；如果它是奇数，那么把 (3n+1) 砍掉一半。这样一直反复砍下去，最后一定在某一步得到 n=1。
# 对给定的任一不超过 1000 的正整数 n，简单地数一下，需要多少步（砍几下）才能得到 n=1？
# 示例：n = 3,(3-5-8-4-2-1)到n=1一共需要5步，则最后输出5
# 卡拉兹猜想 => 函数实现


def callatz(target: int):
	times = 0
	while target != 1:
		if target % 2 != 0:
			target = target * 3 + 1
		target /= 2
		times += 1
	return times  # 输出他


target = int(input())
#  调用他
print(callatz(target))
