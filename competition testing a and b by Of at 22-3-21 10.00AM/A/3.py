# encoding: utf-8 #
"""
==========
File Name:              3                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:                         
==========
"""
# 输入一个正整数，输出这个正整数的的阶乘。
# 阶乘的定义：一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积。比如：5的阶乘为（5*4*3*2*1）120

# 我们可以利用阶乘的特性，用for累计*=求得
# 当然，要先输入(int)
fact = int(input())


# 来个函数调用一下
def factorial(dest: int):
	count = 0  # 累“加”器
	for i in range(1, dest + 1):  # 注意要从1开始×，所以结束要+1
		count *= i  # 请划重点(too easy)
	return count  # 返回他


# 调用他
print(factorial(fact))
