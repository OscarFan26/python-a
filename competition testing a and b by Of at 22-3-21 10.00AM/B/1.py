# encoding: utf-8 #
"""
==========
File Name:              1                    
Author:                 Oscar Fan
Date:                   2022/3/21
requirements:                         
==========
"""

# 你是否被这个简单的算法所疑惑？
# 最大公因数

def hcf(x, y):
	smaller = y if x > y else x
	for i in range(1, smaller + 1):
		if (x % i == 0) and (y % i == 0):
			answer = i

	return answer


# 用户输入两个数字
num1 = int(input())
num2 = int(input())
print(hcf(num1, num2))
