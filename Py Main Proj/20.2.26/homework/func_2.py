# 定义一个函数，接收一个参数n，函数返回n的阶乘结果！（比如5的阶乘是1*2*3*4*5)
def factorial(n):
	Sum = 1
	for i in range(1, n + 1):
		Sum *= i
	print(Sum)


ask = int(input('请输入一个数字：'))
factorial(ask)
