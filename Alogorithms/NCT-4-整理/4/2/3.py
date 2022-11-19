# encoding: utf-8 #
"""
==========
File Name:              3                    
Author:                 Oscar Fan
Date:                   2022/4/14
requirements:                         
==========
"""
"""
已知主串 s1 和子串 s2 如下所示，请使用BF算法编写程序，找到子串在主串中的位置并打印到控制台。

s1 = "qazxcdewsjkl"
s2 = "dews"
"""


def BF(s1, s2):
	"""
	:param s1: 主串
	:param s2: 子串
	:return:
	"""
	for i in range(len(s1) - len(s2) + 1):
		if s1[i:i + len(s2)] == s2:
			print(i)


# 0 1 2 3
#     2 3
# i all: 0 - 3 （0, 1, 2)
# i = 0: s1[0: 0+2] （0, 1)
#  0, 1 != 2, 3
# 1: ...
# 2: s1[2: 2+2] （2, 3) (不到2+2)
#  2, 3 == 2, 3
#  over


BF("qazxcdewsjkl", "dews")
