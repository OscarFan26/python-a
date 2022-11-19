# encoding: utf-8 #
"""
==========
File Name:              2                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:                         
==========
"""


# 这么简单还看？？？uh？


def exchange(targ: list):
	targ[0], targ[-1] = targ[-1], targ[0]


target = eval(input())  # 这可能对你有点难，不会查资料，这样可以保持输入是list
print(exchange(target))
